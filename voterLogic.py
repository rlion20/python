from PyQt6.QtWidgets import *
from math import *
from voterGui import Ui_MainWi

class voterLogic():
    def __init__(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def voteFunction(self):
        if self.numberWhoVoting == 1:
            self.numberWhoVoting +=1


