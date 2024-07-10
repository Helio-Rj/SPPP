# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sppp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
    QVBoxLayout, QWidget)
import logow_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(316, 474)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"background-color: rgb(170, 255, 127);")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.main_frame)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.top_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.logo_label = QLabel(self.top_frame)
        self.logo_label.setObjectName(u"logo_label")
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.logo_label.setFont(font)
        self.logo_label.setStyleSheet(u"font: 87 12pt \"Arial Black\";")
        self.logo_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.logo_label)

        self.btn_gerar_palpite = QPushButton(self.top_frame)
        self.btn_gerar_palpite.setObjectName(u"btn_gerar_palpite")
        self.btn_gerar_palpite.setMinimumSize(QSize(160, 31))
        self.btn_gerar_palpite.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gerar_palpite.setStyleSheet(u"QPushButton:hover{	\n"
"	color: rgb(0, 0, 0);\n"
"	\n"
"	background-color: rgb(85, 255, 127);\n"
"	\n"
"	\n"
"\n"
"	color: #000000f	\n"
"	\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	font: 87 8pt \"Arial Black\";	\n"
"	\n"
"	background-color: rgb(51, 146, 90);\n"
"\n"
"	\n"
"	\n"
"	color: #fff\n"
"	\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.btn_gerar_palpite)


        self.verticalLayout.addWidget(self.top_frame)

        self.down_frame = QFrame(self.main_frame)
        self.down_frame.setObjectName(u"down_frame")
        self.down_frame.setStyleSheet(u"")
        self.down_frame.setFrameShape(QFrame.StyledPanel)
        self.down_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.down_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.entry_1 = QLineEdit(self.down_frame)
        self.entry_1.setObjectName(u"entry_1")
        self.entry_1.setStyleSheet(u"font: 87 10pt \"Arial Black\";\n"
"background-color: rgb(51, 146, 90);\n"
"color: #ffffff")
        self.entry_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.entry_1)

        self.entry_2 = QLineEdit(self.down_frame)
        self.entry_2.setObjectName(u"entry_2")
        self.entry_2.setStyleSheet(u"font: 87 10pt \"Arial Black\";\n"
"background-color: rgb(51, 146, 90);\n"
"color: #ffffff")
        self.entry_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.entry_2)

        self.entry_3 = QLineEdit(self.down_frame)
        self.entry_3.setObjectName(u"entry_3")
        self.entry_3.setStyleSheet(u"font: 87 10pt \"Arial Black\";\n"
"background-color: rgb(51, 146, 90);\n"
"color: #ffffff")
        self.entry_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.entry_3)

        self.label_info_rodape = QLabel(self.down_frame)
        self.label_info_rodape.setObjectName(u"label_info_rodape")
        self.label_info_rodape.setStyleSheet(u"font: 87 6pt \"Arial Black\";")

        self.verticalLayout_3.addWidget(self.label_info_rodape)


        self.verticalLayout.addWidget(self.down_frame)


        self.horizontalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/logow/Imagens/logo.png\"/></p></body></html>", None))
        self.btn_gerar_palpite.setText(QCoreApplication.translate("MainWindow", u"Gerar Palpite", None))
        self.entry_1.setText("")
        self.entry_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00 - 00 - 00 - 00 - 00 - 00", None))
        self.entry_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00 - 00 - 00 - 00 - 00 - 00", None))
        self.entry_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00 - 00 - 00 - 00 - 00 - 00", None))
        self.label_info_rodape.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:7pt; font-weight:600; color:#0000ff;\">Boa Sorte !</span></p></body></html>", None))
    # retranslateUi

