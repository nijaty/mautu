#!/bin/bash
# Build a .deb package for MAUTU.
# Usage: bash scripts/build_deb.sh [VERSION]
set -e

VERSION="${1:-$(date +'%Y.%m.%d')}"
PKG_NAME="mautu"
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PKG_DIR="${ROOT_DIR}/dist/${PKG_NAME}_${VERSION}"

echo "Building ${PKG_NAME} ${VERSION}..."

# ── Clean previous build ────────────────────────────────────────────────────
rm -rf "${PKG_DIR}"

# ── Directory structure ──────────────────────────────────────────────────────
mkdir -p "${PKG_DIR}/DEBIAN"
mkdir -p "${PKG_DIR}/usr/share/mautu"
mkdir -p "${PKG_DIR}/usr/bin"
mkdir -p "${PKG_DIR}/usr/share/applications"

# ── Copy application files ───────────────────────────────────────────────────
rsync -a --exclude='venv/' --exclude='__pycache__/' --exclude='*.pyc' \
    --exclude='dist/' --exclude='.git/' --exclude='data/docs.db' \
    --exclude='config/database.ini' \
    "${ROOT_DIR}/" "${PKG_DIR}/usr/share/mautu/"

# ── Main launcher (/usr/bin/mautu) ───────────────────────────────────────────
cat > "${PKG_DIR}/usr/bin/mautu" << 'EOF'
#!/bin/bash
cd /usr/share/mautu
exec /usr/share/mautu/venv/bin/python3 -B /usr/share/mautu/main.py "$@"
EOF
chmod 755 "${PKG_DIR}/usr/bin/mautu"

# ── Manual import helper (/usr/bin/mautu-import-manuals) ────────────────────
cat > "${PKG_DIR}/usr/bin/mautu-import-manuals" << 'EOF'
#!/bin/bash
cd /usr/share/mautu
exec /usr/share/mautu/venv/bin/python3 /usr/share/mautu/scripts/import_manuals.py "$@"
EOF
chmod 755 "${PKG_DIR}/usr/bin/mautu-import-manuals"

# ── Desktop entry ────────────────────────────────────────────────────────────
cat > "${PKG_DIR}/usr/share/applications/mautu.desktop" << 'EOF'
[Desktop Entry]
Name=MAUTU
Comment=IT Manual Viewer
Exec=mautu
Icon=/usr/share/mautu/icons/logo.png
Terminal=false
Type=Application
Categories=Utility;Documentation;Education;
EOF

# ── DEBIAN control files ─────────────────────────────────────────────────────
cp "${ROOT_DIR}/debian/control"  "${PKG_DIR}/DEBIAN/control"
cp "${ROOT_DIR}/debian/postinst" "${PKG_DIR}/DEBIAN/postinst"
cp "${ROOT_DIR}/debian/prerm"    "${PKG_DIR}/DEBIAN/prerm"

# Stamp the version into the control file
sed -i "s/^Version:.*/Version: ${VERSION}/" "${PKG_DIR}/DEBIAN/control"

chmod 755 "${PKG_DIR}/DEBIAN/postinst"
chmod 755 "${PKG_DIR}/DEBIAN/prerm"

# ── Build ────────────────────────────────────────────────────────────────────
dpkg-deb --build "${PKG_DIR}"

echo ""
echo "Package ready: dist/${PKG_NAME}_${VERSION}.deb"
echo "Install with:  sudo dpkg -i dist/${PKG_NAME}_${VERSION}.deb"
echo "               sudo apt-get install -f   # resolve any missing deps"
