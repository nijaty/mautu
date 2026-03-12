import sys
import os

from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from ui_mautu_new_design import *
from database.db_manager import DatabaseManager
from ui.manual_viewer import ManualViewer
from ui.manual_editor_dialog import ManualEditorDialog
from ui.manual_tree_widget import ManualTreeWidget


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize database
        try:
            self.db_manager = DatabaseManager()
        except Exception as e:
            QMessageBox.critical(self, "Database Error",
                f"Failed to open database:\n{str(e)}")
            sys.exit(1)

        # Setup manual viewer
        self.manual_viewer = ManualViewer(self)

        # Replace textEdit with stacked widget containing manual viewer
        self.content_stack = QStackedWidget()
        self.content_stack.addWidget(self.manual_viewer)

        # Replace textEdit in layout
        old_textedit = self.ui.textEdit
        parent_widget = old_textedit.parent()
        parent_layout = parent_widget.layout()

        # Find and replace textEdit in the layout
        for i in range(parent_layout.count()):
            if parent_layout.itemAt(i).widget() == old_textedit:
                parent_layout.removeWidget(old_textedit)
                parent_layout.insertWidget(i, self.content_stack)
                break
        old_textedit.deleteLater()

        # Setup manual tree in toolBox
        self.manual_tree = ManualTreeWidget(self.db_manager)

        # Add manual tree to toolBox (replace first page or add new page)
        # We'll add it as a new page
        self.ui.toolBox.addItem(self.manual_tree, "")

        # Connect signals
        self.manual_tree.manual_selected.connect(self.display_manual)
        self.ui.lineEdit.textChanged.connect(self.on_search_text_changed)
        self.ui.lineEdit.returnPressed.connect(self.on_search_button_clicked)
        self.ui.pushButton_4.clicked.connect(self.on_search_button_clicked)

        # Watch manuals/ directory for file changes and auto-reimport
        self._manuals_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'manuals')
        self._file_watcher = QFileSystemWatcher()
        self._watch_manuals_dir()
        self._file_watcher.fileChanged.connect(self._on_manual_changed)
        self._file_watcher.directoryChanged.connect(self._on_manual_changed)

        # Existing setup
        self.ui.slide_part.setMaximumWidth(0)
        self.ui.slide_part.setMinimumWidth(0)

        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        QSizeGrip(self.ui.size_grip)

        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())
        self.ui.close_window_button.clicked.connect(lambda: self.close())

        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())

        self.ui.github_button.clicked.connect(self.open_mautu_github)

        # Make header draggable by setting up mouse event handling
        if hasattr(self.ui, 'header'):
            self.ui.header.mousePressEvent = self.header_mousePressEvent

        self.ui.open_close_side_btn.clicked.connect(lambda: self.slideLeftMenu())

        # F5 — manual refresh
        QShortcut(QKeySequence("F5"), self).activated.connect(self.refresh_manuals)

        self.show()

    def _watch_manuals_dir(self):
        """Register every subdirectory and .md file with the file watcher."""
        if not os.path.isdir(self._manuals_dir):
            return
        for root, dirs, files in os.walk(self._manuals_dir):
            self._file_watcher.addPath(root)
            for f in files:
                if f.endswith('.md'):
                    self._file_watcher.addPath(os.path.join(root, f))

    def refresh_manuals(self):
        """Full sync: wipe DB manuals and reimport from manuals/ folder."""
        self.db_manager.sync_from_disk(self._manuals_dir)
        self.manual_tree.refresh()
        self._watch_manuals_dir()

    def _on_manual_changed(self, path):
        """Called by file watcher when any .md file changes."""
        self.refresh_manuals()

    def header_mousePressEvent(self, event):
        """Handle mouse press on header for window dragging"""
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            # Walk up from the deepest child to detect interactive widgets
            # (childAt returns the deepest descendant, which may be nested inside frames)
            widget = self.ui.header.childAt(event.position().toPoint())
            w = widget
            while w is not None and w is not self.ui.header:
                if isinstance(w, (QPushButton, QLineEdit, QTextEdit, QComboBox)):
                    return
                w = w.parent()
            # Use system move for Wayland compatibility
            if self.windowHandle():
                self.windowHandle().startSystemMove()
            event.accept()


    ########################################################################
    # Slide left menu function
    ########################################################################
    def slideLeftMenu(self):
        # Get current maximum width of the slide menu
        width = self.ui.slide_part.maximumWidth()

        # Toggle between expanded and collapsed
        newWidth = 0 if width > 0 else 400

        # Change icon based on the state
        if newWidth == 0:
            self.ui.open_close_side_btn.setIcon(QtGui.QIcon(u":/icons/icons/menu-burger.png"))
        else:
            self.ui.open_close_side_btn.setIcon(QtGui.QIcon(u":/icons/icons/angle-small-left.png"))

        # Animate the transition
        self.animation = QPropertyAnimation(self.ui.slide_part, QtCore.QByteArray(b"maximumWidth"))
        self.animation.setDuration(900)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animation.start()

    #######################################################################

    def open_mautu_github(self):
        QDesktopServices.openUrl(QUrl("https://github.com/nijaty/mautu"))

    def restore_or_maximize_window(self):
        # If window is maximized
        if self.isMaximized():
            self.showNormal()
            # Change Icon
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/icons/window-maximize.png"))
        else:
            self.showMaximized()
            # Change Icon
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/icons/window-restore.png"))

    def display_manual(self, manual_id):
        """Display a manual in the viewer."""
        manual_data = self.db_manager.get_manual_by_id(manual_id)
        if manual_data:
            self.manual_viewer.set_content(manual_data)
            self.content_stack.setCurrentWidget(self.manual_viewer)

    def on_search_text_changed(self, text):
        """Real-time filtering (placeholder for future enhancement)."""
        pass

    def on_search_button_clicked(self):
        """Full-text search through manual content."""
        query = self.ui.lineEdit.text().strip()
        if query:
            results = self.db_manager.search_manuals(query)
            if results:
                # Display first result
                self.display_manual(results[0][0])
            else:
                QMessageBox.information(self, "Search Results",
                    f"No manuals found matching '{query}'")

    def open_manual_editor(self, manual_id=None):
        """Open the manual editor dialog."""
        dialog = ManualEditorDialog(self.db_manager, manual_id, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.manual_tree.refresh()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())