import icons_rc  # noqa: F401 — registers Qt resources
from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QIcon

_CATEGORY_ICONS = {
    'QA': ':/icons/icons/qa_logo.png',
    'Git': ':/icons/icons/github_logo.png',
    'RHEL': ':/icons/icons/rhel_logo.png',
    'Linux': ':/icons/icons/linux_logo.png',
    'Docker':  ':/icons/icons/docker_logo.png',
    'DevOps':  ':/icons/icons/devops_logo.png',
    'Ubuntu': ':icons/icons/ubuntu_logo.png',
    'Windows': ':/icons/icons/windows_logo.png',
    'Backend': ':/icons/icons/backend_logo.png',
    'Network': ':/icons/icons/network_logo.png',
    'Ansible': ':/icons/icons/ansible_logo.png',
    'Frontend': ':/icons/icons/frontend_logo.png',
    'DataBase': ':/icons/icons/database_logo.png',
    'SysAdmin': ':/icons/icons/sysadmin_logo.png',
    'Kubernetes': ':/icons/icons/kubernetes_logo.png',
    'Terraform': ':/icons/icons/terraform_logo.png',
    'Development': ':/icons/icons/development_logo.png',
    'CyberSecurity': ':/icons/icons/cybersecurity_logo.png',
}

class ManualTreeWidget(QTreeWidget):
    """Tree widget for displaying hierarchical manual categories and items."""

    manual_selected = Signal(int)  # Emits manual_id when a manual is clicked

    def __init__(self, db_manager, parent=None):
        super().__init__(parent)
        self.db_manager = db_manager
        self.setHeaderHidden(True)
        self.setStyleSheet("""
            QTreeWidget {
                background-color: rgb(112, 163, 94);
                color: rgb(42, 44, 53);
                font-weight: bold;
                font-size: 17px;
                border: none;
            }
            QTreeWidget::item {
                padding: 5px;
            }
            QTreeWidget::item:selected {
                background-color: rgba(255, 255, 255, 0.2);
            }
            QTreeWidget::item:hover {
                background-color: rgba(255, 255, 255, 0.1);
            }
        """)

        self.itemClicked.connect(self.on_item_clicked)
        self.load_tree()

    def load_tree(self):
        """Load category tree with manuals from database."""
        self.clear()
        categories = self.db_manager.get_categories_tree()

        # Build tree structure
        items_map = {}

        # First pass: create all category items
        for cat_id, name, parent_id, _ in categories:
            item = QTreeWidgetItem([name])
            item.setData(0, Qt.ItemDataRole.UserRole, {'type': 'category', 'id': cat_id})
            if name in _CATEGORY_ICONS:
                item.setIcon(0, QIcon(_CATEGORY_ICONS[name]))
            items_map[cat_id] = item

            if parent_id is None:
                self.addTopLevelItem(item)
            else:
                if parent_id in items_map:
                    items_map[parent_id].addChild(item)

        # Second pass: add manuals to leaf categories
        for cat_id, item in items_map.items():
            if item.childCount() == 0:  # Leaf category
                manuals = self.db_manager.get_manuals_by_category(cat_id)
                for manual_id, title, _, _, _ in manuals:
                    manual_item = QTreeWidgetItem([title])
                    manual_item.setData(0, Qt.ItemDataRole.UserRole,
                                       {'type': 'manual', 'id': manual_id})
                    item.addChild(manual_item)

        self.collapseAll()

    def on_item_clicked(self, item, column):
        """Handle tree item click.

        Args:
            item: The clicked QTreeWidgetItem
            column: The column index
        """
        data = item.data(0, Qt.ItemDataRole.UserRole)
        if data and data['type'] == 'manual':
            self.manual_selected.emit(data['id'])

    def refresh(self):
        """Reload the tree from database."""
        self.load_tree()
