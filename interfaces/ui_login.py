# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'loginIqPOWK.ui'
##
# Created by: Qt User Interface Compiler version 6.8.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QWidget)
import resources_rc


class Ui_LoginUI(object):
    def setupUi(self, LoginUI):
        if not LoginUI.objectName():
            LoginUI.setObjectName(u"LoginUI")
        LoginUI.resize(625, 565)
        icon = QIcon()
        icon.addFile(u":/images/static/logo-Hermes-icon.png",
                     QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        LoginUI.setWindowIcon(icon)
        self.widget = QWidget(LoginUI)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 550, 500))
        self.widget.setStyleSheet(u"QPushButton#loginBtn{\n"
                                  "	background-color:  #007bff;\n"
                                  "	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0B00A9, stop:1 #3D00F5);\n"
                                  "	color: white;\n"
                                  "	border-radius: 5px\n"
                                  "}\n"
                                  "QPushButton#loginBtn:hover{\n"
                                  "	background-color:  #068fff;\n"
                                  "}\n"
                                  "QPushButton#loginBtn:pressed{\n"
                                  "	padding-left: 5px;\n"
                                  "	padding-top: 5px;\n"
                                  "	background-color: red;\n"
                                  "}")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 280, 430))
        self.label.setStyleSheet(u"border-image: url(:/images/static/hermes_inventory.jpeg);\n"
                                 "border-top-left-radius: 50px;\n"
                                 "")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 30, 280, 430))
        self.label_2.setStyleSheet(u"background-color: rgba(0,0,0,80);\n"
                                   "border-top-left-radius: 50px;\n"
                                   "")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 30, 240, 430))
        self.label_3.setStyleSheet(u"background-color: white;\n"
                                   "border-bottom-right-radius: 50px;")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(340, 80, 100, 40))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgba(0,0,0,200)")
        self.usernameTxt = QLineEdit(self.widget)
        self.usernameTxt.setObjectName(u"usernameTxt")
        self.usernameTxt.setGeometry(QRect(295, 150, 190, 40))
        font1 = QFont()
        font1.setPointSize(10)
        self.usernameTxt.setFont(font1)
        self.usernameTxt.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
                                       "border: none;\n"
                                       "border-bottom: 2px solid rgba(46,82,101,200);\n"
                                       "color: rgba(0,0,0,240);\n"
                                       "padding-bottom: 7px;")
        self.passwordTxt = QLineEdit(self.widget)
        self.passwordTxt.setObjectName(u"passwordTxt")
        self.passwordTxt.setGeometry(QRect(295, 215, 190, 40))
        self.passwordTxt.setFont(font1)
        self.passwordTxt.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
                                       "border: none;\n"
                                       "border-bottom: 2px solid rgba(46,82,101,200);\n"
                                       "color: rgba(0,0,0,240);\n"
                                       "padding-bottom: 7px;")
        self.passwordTxt.setEchoMode(QLineEdit.EchoMode.Password)
        self.loginBtn = QPushButton(self.widget)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setGeometry(QRect(295, 295, 190, 40))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.loginBtn.setFont(font2)
        self.loginBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.closeBtn = QPushButton(self.widget)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setGeometry(QRect(485, 30, 25, 25))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.closeBtn.setFont(font3)
        self.closeBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.closeBtn.setStyleSheet(u"border: none;\n"
                                    "")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 310, 230, 131))
        self.label_6.setStyleSheet(
            u"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0B00A9, stop:1 #3D00F5);")
        self.logo_2 = QLabel(self.widget)
        self.logo_2.setObjectName(u"logo_2")
        self.logo_2.setGeometry(QRect(80, 300, 150, 150))
        self.logo_2.setStyleSheet(
            u"border-image: url(:/images/static/logo-Hermes-white-tranparent.png);")

        self.retranslateUi(LoginUI)

        QMetaObject.connectSlotsByName(LoginUI)
    # setupUi

    def retranslateUi(self, LoginUI):
        LoginUI.setWindowTitle(QCoreApplication.translate(
            "LoginUI", u"Login - Hermes", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate(
            "LoginUI", u"Log In", None))
        self.usernameTxt.setPlaceholderText(
            QCoreApplication.translate("LoginUI", u"Nombre de Usuario", None))
        self.passwordTxt.setPlaceholderText(
            QCoreApplication.translate("LoginUI", u"Contrase\u00f1a", None))
        self.loginBtn.setText(QCoreApplication.translate(
            "LoginUI", u"Acceder", None))
        self.closeBtn.setText(
            QCoreApplication.translate("LoginUI", u"x", None))
        self.label_6.setText("")
        self.logo_2.setText("")
    # retranslateUi
