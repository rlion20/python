from PyQt6.QtWidgets import *
from math import *
from tvGui import Ui_MainWindow

class tvLogic():
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.volumeUpButton.clicked.connect(self.volumeFunction())
        self.volumeDownButton.clicked.connect(self.volumeFunction())
        self.muteButton.clicked.connect(self.muteFunction)



    def volumeFunction(self):
        if self.volumeUpButton.isChecked():
            self.volume +=1



    def channelFunction(self):



    def muteFunction(self):

