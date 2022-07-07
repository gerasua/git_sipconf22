# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 720)
        MainWindow.setMinimumSize(QSize(1000, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush11 = QBrush(QColor(51, 153, 255, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush11)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.verticalLayout_13 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"image: url(:/16x16/icons/16x16/ct-settings.png);")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(u"image: url(:/48x48/icons/48x48/ct-settings.png);")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 100))
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_empresa = QWidget()
        self.page_empresa.setObjectName(u"page_empresa")
        self.verticalLayout_10 = QVBoxLayout(self.page_empresa)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_4 = QFrame(self.page_empresa)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 70))
        self.frame_4.setMaximumSize(QSize(16777215, 70))
        self.frame_4.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_4)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label)


        self.verticalLayout_19.addLayout(self.verticalLayout_17)


        self.verticalLayout_10.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.page_empresa)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_2.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_2.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_2.setHorizontalSpacing(60)
        self.formLayout_2.setVerticalSpacing(60)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_7)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(300, 0))
        self.label_6.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(300, 0))
        self.label_7.setStyleSheet(u"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_7.setFrameShape(QFrame.NoFrame)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.label_7)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(4, QFormLayout.LabelRole, self.verticalSpacer_8)

        self.btn_datos_sucursal = QPushButton(self.frame_5)
        self.btn_datos_sucursal.setObjectName(u"btn_datos_sucursal")
        self.btn_datos_sucursal.setMinimumSize(QSize(300, 100))
        self.btn_datos_sucursal.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/80x80/icons/80x80/ct-sucursal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_datos_sucursal.setIcon(icon3)
        self.btn_datos_sucursal.setIconSize(QSize(300, 100))

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.btn_datos_sucursal)

        self.btn_datos_empresa = QPushButton(self.frame_5)
        self.btn_datos_empresa.setObjectName(u"btn_datos_empresa")
        self.btn_datos_empresa.setMinimumSize(QSize(300, 100))
        self.btn_datos_empresa.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/80x80/icons/80x80/ct-enterprise2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_datos_empresa.setIcon(icon4)
        self.btn_datos_empresa.setIconSize(QSize(300, 100))

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.btn_datos_empresa)


        self.verticalLayout_18.addLayout(self.formLayout_2)


        self.verticalLayout_10.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.page_empresa)
        self.page_tipo_pesada = QWidget()
        self.page_tipo_pesada.setObjectName(u"page_tipo_pesada")
        self.verticalLayout_16 = QVBoxLayout(self.page_tipo_pesada)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_9 = QFrame(self.page_tipo_pesada)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 70))
        self.frame_9.setMaximumSize(QSize(16777215, 70))
        self.frame_9.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_9)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_11)


        self.verticalLayout_23.addLayout(self.verticalLayout_29)


        self.verticalLayout_16.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.page_tipo_pesada)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_10)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_3.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_3.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_3.setHorizontalSpacing(60)
        self.formLayout_3.setVerticalSpacing(60)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_3.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_3)

        self.btn_pesada = QPushButton(self.frame_10)
        self.btn_pesada.setObjectName(u"btn_pesada")
        self.btn_pesada.setMinimumSize(QSize(300, 100))
        self.btn_pesada.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/24x24/icons/24x24/ct-romana5.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pesada.setIcon(icon5)
        self.btn_pesada.setIconSize(QSize(80, 80))

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.btn_pesada)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_3.setItem(2, QFormLayout.LabelRole, self.verticalSpacer_4)


        self.verticalLayout_26.addLayout(self.formLayout_3)


        self.verticalLayout_16.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.page_tipo_pesada)
        self.page_puertos = QWidget()
        self.page_puertos.setObjectName(u"page_puertos")
        self.verticalLayout_30 = QVBoxLayout(self.page_puertos)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_12 = QFrame(self.page_puertos)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 70))
        self.frame_12.setMaximumSize(QSize(16777215, 70))
        self.frame_12.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_12)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_12 = QLabel(self.frame_12)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 0))
        self.label_12.setMaximumSize(QSize(16777215, 16777215))
        self.label_12.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_12)


        self.verticalLayout_32.addLayout(self.verticalLayout_31)


        self.verticalLayout_30.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.page_puertos)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_5.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_5.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_5.setHorizontalSpacing(60)
        self.formLayout_5.setVerticalSpacing(60)
        self.btn_serialindicador = QPushButton(self.frame_13)
        self.btn_serialindicador.setObjectName(u"btn_serialindicador")
        self.btn_serialindicador.setMinimumSize(QSize(300, 100))
        self.btn_serialindicador.setMaximumSize(QSize(300, 100))
        self.btn_serialindicador.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/80x80/icons/80x80/ct-indicador.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_serialindicador.setIcon(icon6)
        self.btn_serialindicador.setIconSize(QSize(80, 80))

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.btn_serialindicador)

        self.btn_serialimpresora = QPushButton(self.frame_13)
        self.btn_serialimpresora.setObjectName(u"btn_serialimpresora")
        self.btn_serialimpresora.setMinimumSize(QSize(300, 100))
        self.btn_serialimpresora.setMaximumSize(QSize(300, 100))
        self.btn_serialimpresora.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/80x80/icons/80x80/ct-impresora.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_serialimpresora.setIcon(icon7)
        self.btn_serialimpresora.setIconSize(QSize(80, 80))

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.btn_serialimpresora)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_5.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_5)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_5.setItem(2, QFormLayout.LabelRole, self.verticalSpacer_6)


        self.horizontalLayout_15.addLayout(self.formLayout_5)


        self.verticalLayout_30.addWidget(self.frame_13)

        self.stackedWidget.addWidget(self.page_puertos)
        self.page_usuarios = QWidget()
        self.page_usuarios.setObjectName(u"page_usuarios")
        self.verticalLayout_37 = QVBoxLayout(self.page_usuarios)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.frame_15 = QFrame(self.page_usuarios)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 70))
        self.frame_15.setMaximumSize(QSize(16777215, 70))
        self.frame_15.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_15)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_14 = QLabel(self.frame_15)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_39.addWidget(self.label_14)


        self.verticalLayout_38.addLayout(self.verticalLayout_39)


        self.verticalLayout_37.addWidget(self.frame_15)

        self.frame_11 = QFrame(self.page_usuarios)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 70))
        self.frame_11.setMaximumSize(QSize(16777215, 70))
        self.frame_11.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buscarUsuarios = QLineEdit(self.frame_11)
        self.buscarUsuarios.setObjectName(u"buscarUsuarios")
        self.buscarUsuarios.setMinimumSize(QSize(0, 30))
        self.buscarUsuarios.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.buscarUsuarios.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.buscarUsuarios)

        self.btnBuscarUsuario = QPushButton(self.frame_11)
        self.btnBuscarUsuario.setObjectName(u"btnBuscarUsuario")
        self.btnBuscarUsuario.setMinimumSize(QSize(100, 40))
        self.btnBuscarUsuario.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/16x16/icons/16x16/cil-magnifying-glass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnBuscarUsuario.setIcon(icon8)

        self.horizontalLayout.addWidget(self.btnBuscarUsuario)


        self.horizontalLayout_14.addLayout(self.horizontalLayout)


        self.verticalLayout_37.addWidget(self.frame_11)

        self.frame_14 = QFrame(self.page_usuarios)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 120))
        self.frame_14.setMaximumSize(QSize(16777215, 120))
        self.frame_14.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.btnAgregarUsuario = QPushButton(self.frame_14)
        self.btnAgregarUsuario.setObjectName(u"btnAgregarUsuario")
        self.btnAgregarUsuario.setMinimumSize(QSize(90, 100))
        self.btnAgregarUsuario.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/80x80/icons/80x80/ct-usuarios.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAgregarUsuario.setIcon(icon9)
        self.btnAgregarUsuario.setIconSize(QSize(80, 80))

        self.horizontalLayout_16.addWidget(self.btnAgregarUsuario)

        self.btnContraUsuario = QPushButton(self.frame_14)
        self.btnContraUsuario.setObjectName(u"btnContraUsuario")
        self.btnContraUsuario.setMinimumSize(QSize(0, 100))
        self.btnContraUsuario.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/80x80/icons/80x80/ct-contrase\u00f1a.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnContraUsuario.setIcon(icon10)
        self.btnContraUsuario.setIconSize(QSize(80, 80))

        self.horizontalLayout_16.addWidget(self.btnContraUsuario)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_16)


        self.verticalLayout_37.addWidget(self.frame_14)

        self.frame_16 = QFrame(self.page_usuarios)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_16)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.table_usuarios = QTableWidget(self.frame_16)
        if (self.table_usuarios.columnCount() < 3):
            self.table_usuarios.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_usuarios.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_usuarios.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_usuarios.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table_usuarios.setObjectName(u"table_usuarios")
        self.table_usuarios.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_28.addWidget(self.table_usuarios)


        self.verticalLayout_37.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.page_usuarios)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 60))
        self.frame_17.setMaximumSize(QSize(16777215, 60))
        self.frame_17.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer)

        self.btnActualizarTablaUsuarios = QPushButton(self.frame_17)
        self.btnActualizarTablaUsuarios.setObjectName(u"btnActualizarTablaUsuarios")
        self.btnActualizarTablaUsuarios.setMinimumSize(QSize(80, 30))
        self.btnActualizarTablaUsuarios.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/16x16/icons/16x16/cil-loop-circular.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnActualizarTablaUsuarios.setIcon(icon11)

        self.horizontalLayout_20.addWidget(self.btnActualizarTablaUsuarios)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_20)


        self.verticalLayout_37.addWidget(self.frame_17)

        self.stackedWidget.addWidget(self.page_usuarios)
        self.page_camaras_conf = QWidget()
        self.page_camaras_conf.setObjectName(u"page_camaras_conf")
        self.verticalLayout_27 = QVBoxLayout(self.page_camaras_conf)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_18 = QFrame(self.page_camaras_conf)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 70))
        self.frame_18.setMaximumSize(QSize(16777215, 70))
        self.frame_18.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_18)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_13 = QLabel(self.frame_18)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 70))
        self.label_13.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.label_13)


        self.verticalLayout_35.addLayout(self.verticalLayout_33)


        self.verticalLayout_27.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.page_camaras_conf)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_6.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_6.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_6.setHorizontalSpacing(60)
        self.formLayout_6.setVerticalSpacing(60)
        self.btn_camera1 = QPushButton(self.frame_19)
        self.btn_camera1.setObjectName(u"btn_camera1")
        self.btn_camera1.setMinimumSize(QSize(300, 100))
        self.btn_camera1.setMaximumSize(QSize(300, 100))
        self.btn_camera1.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/80x80/icons/80x80/ct-camaras.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_camera1.setIcon(icon12)
        self.btn_camera1.setIconSize(QSize(80, 80))

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.btn_camera1)

        self.btn_camera2 = QPushButton(self.frame_19)
        self.btn_camera2.setObjectName(u"btn_camera2")
        self.btn_camera2.setMinimumSize(QSize(300, 100))
        self.btn_camera2.setMaximumSize(QSize(300, 100))
        self.btn_camera2.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_camera2.setIcon(icon12)
        self.btn_camera2.setIconSize(QSize(80, 80))

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.btn_camera2)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_6.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_9)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_6.setItem(3, QFormLayout.LabelRole, self.verticalSpacer_10)

        self.btn_camera3 = QPushButton(self.frame_19)
        self.btn_camera3.setObjectName(u"btn_camera3")
        self.btn_camera3.setMinimumSize(QSize(300, 100))
        self.btn_camera3.setMaximumSize(QSize(300, 100))
        self.btn_camera3.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_camera3.setIcon(icon12)
        self.btn_camera3.setIconSize(QSize(80, 80))

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.btn_camera3)

        self.btn_camera4 = QPushButton(self.frame_19)
        self.btn_camera4.setObjectName(u"btn_camera4")
        self.btn_camera4.setMinimumSize(QSize(300, 100))
        self.btn_camera4.setMaximumSize(QSize(300, 100))
        self.btn_camera4.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_camera4.setIcon(icon12)
        self.btn_camera4.setIconSize(QSize(80, 80))

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.btn_camera4)


        self.horizontalLayout_17.addLayout(self.formLayout_6)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_17)


        self.verticalLayout_27.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.page_camaras_conf)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 100))
        self.frame_20.setMaximumSize(QSize(16777215, 100))
        self.frame_20.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.btn_back_camaras = QPushButton(self.frame_20)
        self.btn_back_camaras.setObjectName(u"btn_back_camaras")
        self.btn_back_camaras.setMinimumSize(QSize(200, 70))
        self.btn_back_camaras.setMaximumSize(QSize(200, 70))
        self.btn_back_camaras.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/80x80/icons/80x80/ct-regresar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_back_camaras.setIcon(icon13)
        self.btn_back_camaras.setIconSize(QSize(80, 70))

        self.horizontalLayout_22.addWidget(self.btn_back_camaras)


        self.horizontalLayout_23.addLayout(self.horizontalLayout_22)


        self.verticalLayout_27.addWidget(self.frame_20)

        self.stackedWidget.addWidget(self.page_camaras_conf)
        self.page_bascula = QWidget()
        self.page_bascula.setObjectName(u"page_bascula")
        self.verticalLayout_12 = QVBoxLayout(self.page_bascula)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_21 = QFrame(self.page_bascula)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 70))
        self.frame_21.setMaximumSize(QSize(16777215, 70))
        self.frame_21.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_21)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_2 = QLabel(self.frame_21)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.label_2)


        self.verticalLayout_40.addLayout(self.verticalLayout_36)


        self.verticalLayout_12.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.page_bascula)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout.setHorizontalSpacing(60)
        self.formLayout.setVerticalSpacing(60)
        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_13)

        self.btn_Bascula = QPushButton(self.frame_22)
        self.btn_Bascula.setObjectName(u"btn_Bascula")
        self.btn_Bascula.setMinimumSize(QSize(300, 100))
        self.btn_Bascula.setMaximumSize(QSize(300, 100))
        self.btn_Bascula.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/48x48/icons/48x48/ct-romana.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Bascula.setIcon(icon14)
        self.btn_Bascula.setIconSize(QSize(80, 80))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.btn_Bascula)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(2, QFormLayout.LabelRole, self.verticalSpacer_14)


        self.horizontalLayout_24.addLayout(self.formLayout)


        self.verticalLayout_12.addWidget(self.frame_22)

        self.stackedWidget.addWidget(self.page_bascula)
        self.page_camaras = QWidget()
        self.page_camaras.setObjectName(u"page_camaras")
        self.verticalLayout_14 = QVBoxLayout(self.page_camaras)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_23 = QFrame(self.page_camaras)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 70))
        self.frame_23.setMaximumSize(QSize(16777215, 70))
        self.frame_23.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_23)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_3 = QLabel(self.frame_23)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_41.addWidget(self.label_3)


        self.verticalLayout_42.addLayout(self.verticalLayout_41)


        self.verticalLayout_14.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.page_camaras)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.formLayout_9 = QFormLayout()
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.formLayout_9.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_9.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_9.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_9.setHorizontalSpacing(60)
        self.formLayout_9.setVerticalSpacing(60)
        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_9.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_15)

        self.btn_camarasad = QPushButton(self.frame_24)
        self.btn_camarasad.setObjectName(u"btn_camarasad")
        self.btn_camarasad.setMinimumSize(QSize(300, 100))
        self.btn_camarasad.setMaximumSize(QSize(300, 100))
        self.btn_camarasad.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_camarasad.setIcon(icon12)
        self.btn_camarasad.setIconSize(QSize(80, 80))

        self.formLayout_9.setWidget(1, QFormLayout.LabelRole, self.btn_camarasad)

        self.btn_camaras_conf = QPushButton(self.frame_24)
        self.btn_camaras_conf.setObjectName(u"btn_camaras_conf")
        self.btn_camaras_conf.setMinimumSize(QSize(300, 100))
        self.btn_camaras_conf.setMaximumSize(QSize(300, 100))
        self.btn_camaras_conf.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(27, 29, 35);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(240, 240, 240);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(44, 49, 60);\n"
"	border-color: rgb(27, 29, 35);\n"
"	border: 2px solid;\n"
"}")
        self.btn_camaras_conf.setIcon(icon12)
        self.btn_camaras_conf.setIconSize(QSize(80, 80))

        self.formLayout_9.setWidget(1, QFormLayout.FieldRole, self.btn_camaras_conf)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_9.setItem(2, QFormLayout.LabelRole, self.verticalSpacer_16)


        self.horizontalLayout_26.addLayout(self.formLayout_9)


        self.verticalLayout_14.addWidget(self.frame_24)

        self.stackedWidget.addWidget(self.page_camaras)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.verticalLayout_13.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)
        QWidget.setTabOrder(self.btn_toggle_menu, self.btn_datos_empresa)
        QWidget.setTabOrder(self.btn_datos_empresa, self.btn_datos_sucursal)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText("")
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| EMPRESA", None))
        self.label_user_icon.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"DATOS DE EMPRESA Y SUCURSAL", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"DATOS DE LA EMPRESA", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"SUCURSAL", None))
        self.btn_datos_sucursal.setText("")
        self.btn_datos_empresa.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"PESADA MANUAL", None))
        self.btn_pesada.setText(QCoreApplication.translate("MainWindow", u"ACTIVAR/DESACTIVAR", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"CONFIGURACION DE PUERTOS SERIALES", None))
        self.btn_serialindicador.setText(QCoreApplication.translate("MainWindow", u"INDICADOR", None))
        self.btn_serialimpresora.setText(QCoreApplication.translate("MainWindow", u"IMPRESORA", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"USUARIOS", None))
        self.btnBuscarUsuario.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btnAgregarUsuario.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.btnContraUsuario.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        ___qtablewidgetitem = self.table_usuarios.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.table_usuarios.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nombre de Usuario", None));
        ___qtablewidgetitem2 = self.table_usuarios.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nivel", None));
        self.btnActualizarTablaUsuarios.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"SELECCIONA LA CAMARA A CONFIGURAR", None))
        self.btn_camera1.setText(QCoreApplication.translate("MainWindow", u"C\u00c1MARA 1", None))
        self.btn_camera2.setText(QCoreApplication.translate("MainWindow", u"C\u00c1MARA 2", None))
        self.btn_camera3.setText(QCoreApplication.translate("MainWindow", u"C\u00c1MARA 3", None))
        self.btn_camera4.setText(QCoreApplication.translate("MainWindow", u"C\u00c1MARA 4", None))
        self.btn_back_camaras.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DATOS DE LA BASCULA", None))
        self.btn_Bascula.setText(QCoreApplication.translate("MainWindow", u"DATOS BASCULA", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"C\u00c1MARAS", None))
        self.btn_camarasad.setText(QCoreApplication.translate("MainWindow", u"ACTIVAR/DESACTIVAR", None))
        self.btn_camaras_conf.setText(QCoreApplication.translate("MainWindow", u"CONFIGURACI\u00d3N", None))
        self.label_credits.setText("")
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

