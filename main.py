from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow)
from ui_main import Ui_MainWindow
import sys
from api import sorteando
from time import sleep


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("S.P.P.P. - Mega Sena  v4.0")
        appIcon = QIcon(u"Imagens/icones.ico")
        self.setWindowIcon(appIcon)
        #  Dimensionamento da Janela
        self.setGeometry(300, 200, 316, 474)
        self.setMinimumHeight(470)
        self.setMinimumWidth(315)
        self.setMaximumHeight(475)
        self.setMaximumWidth(317)

        self.btn_gerar_palpite.clicked.connect(self.consult_api)

    def consult_api(self):
        campos = sorteando()

        self.entry_1.setText(str(sorteando()).strip('[]').replace(',', ' -'))
        sleep(0.5)
        self.entry_2.setText(str(sorteando()).strip('[]').replace(',', ' -'))
        sleep(0.5)
        self.entry_3.setText(str(sorteando()).strip('[]').replace(',', ' -'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

""" Deploy
 pyinstaller.exe --onefile --windowed --icon=Imagens/icones.ico main.py
 
 1 pyside6-rcc logow.qrc -o logow_rc.py
 2  pyside6-uic sppp.ui -o ui_main.py

"""
