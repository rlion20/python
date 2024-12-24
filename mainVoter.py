

from PyQt6 import QtCore, QtGui, QtWidgets

from voterLogic import *

from voterGui import Ui_MainWindow

def main():
    windowVT = Ui_MainWindow()
    windowVT.setupUi(windowVT)
    windowVT.title("Ryan Long CS2 Final Project ")
    windowVT.geometry('400x230')
    windowVT.resizable(False, False)
    windowVT.show



if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())


