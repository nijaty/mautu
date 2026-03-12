#!/usr/bin/env python3
"""Import manuals from the manuals/ directory into the MAUTU database.

Folder structure maps to categories (arbitrary depth supported):
    manuals/<Category>/<Subcategory>/.../manual-name.md

Usage:
    python3 scripts/import_manuals.py [manuals_dir]
"""

import os
import re
import sys

# Allow running from any working directory
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.db_manager import DatabaseManager


def extract_title(content: str, filename: str) -> str:
    """Return the first H1 heading, or derive a title from the filename."""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return os.path.splitext(filename)[0].replace('-', ' ').replace('_', ' ').title()


def import_manuals(manuals_dir: str) -> None:
    db = DatabaseManager()
    imported = 0
    updated = 0

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
            parent_id = db.get_or_create_category(part, parent_id=parent_id)
        category_id = parent_id

        for filename in md_files:
            filepath = os.path.join(root, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            title = extract_title(content, filename)
            db.upsert_manual(title, category_id, content)
            print(f"  [{'/'.join(parts)}] {title}")
            imported += 1

    db.close()
    print(f"\nDone — {imported} manuals imported/updated.")


if __name__ == '__main__':
    manuals_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'manuals'
    )

    if not os.path.isdir(manuals_dir):
        print(f"Error: directory not found: {manuals_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"Importing manuals from: {manuals_dir}\n")
    import_manuals(manuals_dir)
