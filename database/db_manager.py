import os
import re
import sqlite3
from contextlib import contextmanager

# Store the database in the user's data directory so a normal (non-root)
# user can write to it after installing the .deb package.
_DB_PATH = os.path.join(
    os.environ.get('XDG_DATA_HOME', os.path.expanduser('~/.local/share')),
    'mautu', 'docs.db'
)

_SCHEMA = """
CREATE TABLE IF NOT EXISTS categories (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT    NOT NULL,
    parent_id     INTEGER REFERENCES categories(id) ON DELETE CASCADE,
    display_order INTEGER DEFAULT 0,
    created_at    TEXT    DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS manuals (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    title        TEXT    NOT NULL,
    category_id  INTEGER NOT NULL REFERENCES categories(id) ON DELETE CASCADE,
    content      TEXT,
    created_at   TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at   TEXT DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (title, category_id)
);
"""

_SEED = """
INSERT OR IGNORE INTO categories (id, name, parent_id, display_order) VALUES
(1, 'DevOps',      NULL, 1),
(2, 'Network',     NULL, 2),
(3, 'Development', NULL, 3);
"""


class DatabaseManager:
    def __init__(self, db_path=None):
        self.db_path = db_path or _DB_PATH
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._init_db()

    def _init_db(self):
        """Create tables, seed categories, and import manuals on first run."""
        conn = sqlite3.connect(self.db_path)
        conn.executescript(_SCHEMA + _SEED)
        conn.close()

        manuals_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'manuals'
        )
        if os.path.isdir(manuals_dir):
            self.sync_from_disk(manuals_dir)

    @staticmethod
    def _resolve_image_paths(content, base_dir):
        """Replace relative image paths in markdown with absolute file:// URIs."""
        def _replace(match):
            alt, path = match.group(1), match.group(2)
            if path.startswith(('http://', 'https://', 'data:', 'file://')):
                return match.group(0)
            abs_path = os.path.abspath(os.path.join(base_dir, path))
            return f'![{alt}](file://{abs_path})'
        return re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', _replace, content)

    def sync_from_disk(self, manuals_dir):
        """Wipe all manuals and subcategories, then reimport from manuals_dir."""
        with self.get_connection() as conn:
            conn.execute("DELETE FROM manuals")
            conn.execute("DELETE FROM categories WHERE parent_id IS NOT NULL")
        self._import_manuals_dir(manuals_dir)

    def _import_manuals_dir(self, manuals_dir):
        """Scan manuals/ and upsert every .md file into the database.
        Supports arbitrary folder depth: each folder level becomes a category."""
        for root, dirs, files in os.walk(manuals_dir):
            dirs.sort()
            md_files = sorted(f for f in files if f.endswith('.md') and f != 'README.md')
            if not md_files:
                continue

            parts = [p for p in os.path.relpath(root, manuals_dir).split(os.sep)
                     if p and p != '.']
            if not parts:
                continue

            # Walk the full folder chain, creating each level as a category
            parent_id = None
            for part in parts:
                parent_id = self.get_or_create_category(part, parent_id=parent_id)
            category_id = parent_id

            for filename in md_files:
                with open(os.path.join(root, filename), 'r', encoding='utf-8') as f:
                    content = f.read()
                content = self._resolve_image_paths(content, root)
                match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                title = match.group(1).strip() if match else (
                    os.path.splitext(filename)[0].replace('-', ' ').replace('_', ' ').title()
                )
                self.upsert_manual(title, category_id, content)

    @contextmanager
    def get_connection(self):
        """Context manager that opens a connection and commits or rolls back."""
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def get_categories_tree(self):
        """Return all categories ordered for tree building.

        Returns:
            List of Row: (id, name, parent_id, display_order)
        """
        with self.get_connection() as conn:
            return conn.execute("""
                SELECT id, name, parent_id, display_order
                FROM categories
                ORDER BY parent_id, display_order
            """).fetchall()

    def get_manuals_by_category(self, category_id):
        """Return all manuals for a category.

        Returns:
            List of Row: (id, title, content, created_at, updated_at)
        """
        with self.get_connection() as conn:
            return conn.execute("""
                SELECT id, title, content, created_at, updated_at
                FROM manuals
                WHERE category_id = ?
                ORDER BY title
            """, (category_id,)).fetchall()

    def get_manual_by_id(self, manual_id):
        """Return a single manual.

        Returns:
            Row: (id, title, content, category_name)
        """
        with self.get_connection() as conn:
            return conn.execute("""
                SELECT m.id, m.title, m.content, c.name AS category_name
                FROM manuals m
                JOIN categories c ON m.category_id = c.id
                WHERE m.id = ?
            """, (manual_id,)).fetchone()

    def search_manuals(self, query):
        """Search manuals by title and content using LIKE.

        Returns:
            List of Row: (id, title, category_name, snippet)
        """
        pattern = f'%{query}%'
        with self.get_connection() as conn:
            return conn.execute("""
                SELECT m.id, m.title, c.name AS category_name,
                       substr(m.content, 1, 200) AS snippet
                FROM manuals m
                JOIN categories c ON m.category_id = c.id
                WHERE m.title LIKE ? OR m.content LIKE ?
                ORDER BY
                    CASE WHEN m.title LIKE ? THEN 0 ELSE 1 END,
                    m.title
                LIMIT 50
            """, (pattern, pattern, pattern)).fetchall()

    def save_manual(self, title, category_id, content, manual_id=None):
        """Create or update a manual.

        Returns:
            ID of the saved manual
        """
        with self.get_connection() as conn:
            if manual_id:
                conn.execute("""
                    UPDATE manuals
                    SET title = ?, category_id = ?, content = ?,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE id = ?
                """, (title, category_id, content, manual_id))
                return manual_id
            else:
                cursor = conn.execute("""
                    INSERT INTO manuals (title, category_id, content)
                    VALUES (?, ?, ?)
                """, (title, category_id, content))
                return cursor.lastrowid

    def delete_manual(self, manual_id):
        """Delete a manual by ID."""
        with self.get_connection() as conn:
            conn.execute("DELETE FROM manuals WHERE id = ?", (manual_id,))

    def get_or_create_category(self, name, parent_id=None):
        """Return the ID of a category, creating it if it does not exist.

        Args:
            name: Category name
            parent_id: Parent category ID, or None for top-level

        Returns:
            Category ID (int)
        """
        with self.get_connection() as conn:
            row = conn.execute(
                "SELECT id FROM categories WHERE name = ? AND parent_id IS ?",
                (name, parent_id),
            ).fetchone()
            if row:
                return row[0]
            cursor = conn.execute(
                "INSERT INTO categories (name, parent_id) VALUES (?, ?)",
                (name, parent_id),
            )
            return cursor.lastrowid

    def upsert_manual(self, title, category_id, content):
        """Insert a manual or update its content if title+category already exists.

        Returns:
            ID of the saved manual
        """
        with self.get_connection() as conn:
            cursor = conn.execute("""
                INSERT INTO manuals (title, category_id, content)
                VALUES (?, ?, ?)
                ON CONFLICT (title, category_id)
                DO UPDATE SET content     = excluded.content,
                              updated_at  = CURRENT_TIMESTAMP
            """, (title, category_id, content))
            return cursor.lastrowid

    def close(self):
        """No-op — connections are opened and closed per call."""
        pass
