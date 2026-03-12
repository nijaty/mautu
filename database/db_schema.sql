-- MAUTU Database Schema (SQLite)
-- This file is for reference only. The schema is applied automatically
-- by DatabaseManager._init_db() when the app first runs.

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

-- Top-level categories only. All subcategories are created automatically
-- from the manuals/ folder structure when the app first runs.
INSERT OR IGNORE INTO categories (id, name, parent_id, display_order) VALUES
(1, 'DevOps',      NULL, 1),
(2, 'Network',     NULL, 2),
(3, 'Development', NULL, 3);
