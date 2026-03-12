from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel,
                               QLineEdit, QTextEdit, QComboBox, QPushButton,
                               QMessageBox)
from PySide6.QtCore import Qt

class ManualEditorDialog(QDialog):
    """Dialog for creating and editing manuals."""

    def __init__(self, db_manager, manual_id=None, parent=None):
        super().__init__(parent)
        self.db_manager = db_manager
        self.manual_id = manual_id
        self.setWindowTitle("Add Manual" if manual_id is None else "Edit Manual")
        self.setMinimumSize(600, 500)
        self.setup_ui()

        if manual_id:
            self.load_manual()

    def setup_ui(self):
        """Initialize the dialog UI."""
        layout = QVBoxLayout(self)

        # Title field
        title_layout = QHBoxLayout()
        title_layout.addWidget(QLabel("Title:"))
        self.title_edit = QLineEdit()
        self.title_edit.setPlaceholderText("Enter manual title")
        title_layout.addWidget(self.title_edit)
        layout.addLayout(title_layout)

        # Category selector
        category_layout = QHBoxLayout()
        category_layout.addWidget(QLabel("Category:"))
        self.category_combo = QComboBox()
        self.load_categories()
        category_layout.addWidget(self.category_combo)
        layout.addLayout(category_layout)

        # Content editor
        layout.addWidget(QLabel("Content:"))
        self.content_edit = QTextEdit()
        self.content_edit.setAcceptRichText(False)
        self.content_edit.setPlaceholderText("Enter manual content (supports HTML)")
        layout.addWidget(self.content_edit)

        # Buttons
        button_layout = QHBoxLayout()

        save_btn = QPushButton("Save")
        save_btn.setStyleSheet("""
            QPushButton {
                background-color: rgb(112, 163, 94);
                color: white;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: rgb(92, 143, 74);
            }
        """)
        save_btn.clicked.connect(self.save_manual)
        button_layout.addWidget(save_btn)

        cancel_btn = QPushButton("Cancel")
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: rgb(200, 200, 200);
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: rgb(180, 180, 180);
            }
        """)
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)

        layout.addLayout(button_layout)

    def load_categories(self):
        """Load categories into combo box (only leaf categories)."""
        categories = self.db_manager.get_categories_tree()

        # Build parent-child map
        children = {}
        category_map = {}
        for cat_id, name, parent_id, _ in categories:
            category_map[cat_id] = (name, parent_id)
            if parent_id:
                children[parent_id] = children.get(parent_id, []) + [cat_id]

        # Add only leaf categories (those with no children)
        for cat_id, name, parent_id, _ in categories:
            if cat_id not in children:  # Leaf node
                # Get parent name for display
                parent_name = ""
                if parent_id and parent_id in category_map:
                    parent_name = f"{category_map[parent_id][0]} > "

                display_name = f"{parent_name}{name}"
                self.category_combo.addItem(display_name, cat_id)

    def load_manual(self):
        """Load existing manual data for editing."""
        manual = self.db_manager.get_manual_by_id(self.manual_id)
        if manual:
            manual_id, title, content, category_name = manual
            self.title_edit.setText(title)
            self.content_edit.setPlainText(content)

            # Try to find and select the correct category
            # This is a simplified approach - finds by category name
            for i in range(self.category_combo.count()):
                if category_name in self.category_combo.itemText(i):
                    self.category_combo.setCurrentIndex(i)
                    break

    def save_manual(self):
        """Save the manual to database."""
        title = self.title_edit.text().strip()
        content = self.content_edit.toPlainText().strip()
        category_id = self.category_combo.currentData()

        if not title:
            QMessageBox.warning(self, "Validation Error", "Title is required")
            return

        if not content:
            QMessageBox.warning(self, "Validation Error", "Content is required")
            return

        if not category_id:
            QMessageBox.warning(self, "Validation Error", "Please select a category")
            return

        try:
            self.db_manager.save_manual(title, category_id, content, self.manual_id)
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save manual: {str(e)}")
