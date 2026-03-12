# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mautu_new_design.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTextEdit, QToolBox, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(930, 593)
        MainWindow.setStyleSheet(u"*{\n"
"border: none\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slide_part = QFrame(self.centralwidget)
        self.slide_part.setObjectName(u"slide_part")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slide_part.sizePolicy().hasHeightForWidth())
        self.slide_part.setSizePolicy(sizePolicy)
        self.slide_part.setMaximumSize(QSize(0, 16777215))
        self.slide_part.setStyleSheet(u"background-color: rgb(222, 221, 218);")
        self.slide_part.setFrameShape(QFrame.StyledPanel)
        self.slide_part.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.slide_part)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(15, 18, 0, 0)
        self.slide_menu = QFrame(self.slide_part)
        self.slide_menu.setObjectName(u"slide_menu")
        self.slide_menu.setMinimumSize(QSize(398, 0))
        self.slide_menu.setStyleSheet(u"background-color: rgb(112, 163, 94);\n"
"border-top-left-radius: 20px;\n"
"")
        self.slide_menu.setFrameShape(QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.slide_menu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.slide_menu)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 30, 0, 0)
        self.pushButton_7 = QPushButton(self.frame_8)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"background-color: rgb(112, 163, 94);")
        icon = QIcon()
        icon.addFile(u":/icons/icons/front_logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QSize(180, 212))

        self.verticalLayout_9.addWidget(self.pushButton_7, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.frame_8, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_7 = QFrame(self.slide_menu)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setMaximumSize(QSize(16777215, 16777215))
        self.frame_7.setStyleSheet(u"background-color: rgb(112, 163, 94);")
        self.frame_7.setFrameShape(QFrame.HLine)
        self.frame_7.setFrameShadow(QFrame.Plain)
        self.frame_7.setLineWidth(10)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(self.frame_7)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setEnabled(True)
        palette = QPalette()
        brush = QBrush(QColor(112, 163, 94, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        self.toolBox.setPalette(palette)
        self.toolBox.setMouseTracking(False)
        self.toolBox.setAutoFillBackground(False)
        self.toolBox.setStyleSheet(u"QToolBox{\n"
"	background-color: rgb(112, 163, 94);\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"	border-radius: 5px;\n"
"	background-color:  rgb(112, 163, 94);\n"
"}")
        self.toolBox.setFrameShape(QFrame.WinPanel)
        self.toolBox.setFrameShadow(QFrame.Plain)
        self.toolBox.setLineWidth(0)

        self.verticalLayout_6.addWidget(self.toolBox)


        self.verticalLayout_5.addWidget(self.frame_7)


        self.horizontalLayout_7.addWidget(self.slide_menu)


        self.horizontalLayout.addWidget(self.slide_part)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"background-color: rgb(222, 221, 218);")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 18, 15, 0)
        self.header = QFrame(self.main_body)
        self.header.setObjectName(u"header")
        self.header.setStyleSheet(u"background-color: rgb(42, 44, 53);\n"
"border-top-right-radius: 20px;")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(15, 9, 0, 0)
        self.open_close_side_btn = QPushButton(self.frame)
        self.open_close_side_btn.setObjectName(u"open_close_side_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/menu-burger.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.open_close_side_btn.setIcon(icon1)
        self.open_close_side_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.open_close_side_btn)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignLeft|Qt.AlignTop)

        self.search = QFrame(self.header)
        self.search.setObjectName(u"search")
        self.search.setStyleSheet(u"background-color: rgb(42, 44, 53);\n"
"")
        self.search.setFrameShape(QFrame.StyledPanel)
        self.search.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.search)
        self.horizontalLayout_6.setSpacing(9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 11, 0, 0)
        self.lineEdit = QLineEdit(self.search)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(300, 44))
        self.lineEdit.setStyleSheet(u"border-bottom: 3px solid rgb(112, 163, 94);\n"
"font: 57 14pt \"Ubuntu\";\n"
"background-color: rgb(42, 44, 53);\n"
"color: rgb(112, 163, 94);\n"
"padding: 4px 6px;")

        self.horizontalLayout_6.addWidget(self.lineEdit, 0, Qt.AlignHCenter)

        self.pushButton_4 = QPushButton(self.search)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(22, 22))
        self.pushButton_4.setAutoDefault(False)

        self.horizontalLayout_6.addWidget(self.pushButton_4)

        self.pushButton_4.raise_()
        self.lineEdit.raise_()

        self.horizontalLayout_2.addWidget(self.search, 0, Qt.AlignTop)

        self.functional = QFrame(self.header)
        self.functional.setObjectName(u"functional")
        self.functional.setFrameShape(QFrame.StyledPanel)
        self.functional.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.functional)
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 15, 27, 3)
        self.minimize_window_button = QPushButton(self.functional)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/window-minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize_window_button.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.functional)
        self.restore_window_button.setObjectName(u"restore_window_button")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/window-maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restore_window_button.setIcon(icon4)

        self.horizontalLayout_4.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.functional)
        self.close_window_button.setObjectName(u"close_window_button")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/cross.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_window_button.setIcon(icon5)

        self.horizontalLayout_4.addWidget(self.close_window_button)


        self.horizontalLayout_2.addWidget(self.functional, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header)

        self.body = QFrame(self.main_body)
        self.body.setObjectName(u"body")
        sizePolicy1.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy1)
        self.body.setStyleSheet(u"background-color: rgb(42, 44, 53);\n"
"")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.body)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, 12, 22, 10)
        self.textEdit = QTextEdit(self.body)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"background-color: rgb(222, 221, 218);\n"
"border-top-left-radius: 20px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"padding: 10px;")

        self.verticalLayout_7.addWidget(self.textEdit)


        self.verticalLayout.addWidget(self.body)

        self.footer = QFrame(self.main_body)
        self.footer.setObjectName(u"footer")
        self.footer.setStyleSheet(u"background-color: rgb(42, 44, 53);")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 9)
        self.frame_4 = QFrame(self.footer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(21, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(112, 163, 94);")

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.footer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.github_button = QPushButton(self.frame_5)
        self.github_button.setObjectName(u"github_button")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/github_url.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.github_button.setIcon(icon6)
        self.github_button.setIconSize(QSize(22, 22))

        self.verticalLayout_4.addWidget(self.github_button)


        self.horizontalLayout_3.addWidget(self.frame_5)

        self.size_grip = QFrame(self.footer)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.size_grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_7.setText("")
        self.open_close_side_btn.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 \u0432 \u041c\u0430\u0439\u0442\u0438", None))
        self.pushButton_4.setText("")
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"MAUTU v0.0.1", None))
        self.github_button.setText("")
    # retranslateUi

