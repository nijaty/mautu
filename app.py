from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QPixmap
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("МАЙТИ - Мануал для айтишника")
        self.setWindowIcon(QIcon('images/logo.png'))

        label = QLabel(self)
        label.move(600, 50)
        pixmap = QPixmap('images/logo.png')
        label.setPixmap(pixmap)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())

