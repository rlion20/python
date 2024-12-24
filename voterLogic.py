##What's imported



from PyQt6.QtWidgets import *

from voterGui import Ui_MainWindow

##Class

class voterLogic(QMainWindow, Ui_MainWindow):
    choice1 = 0
    choice2 = 0
    choice3 = 0
    names = []

    ##Standard Innit method

    def __init__(self):
        super().__init__()
        splint = Ui_MainWindow()
        splint.setupUi(self)
        spinbox = self.ui.numberWhoVoting
        spinbox.setMinimum(0)
        spinbox.setMaximum(3)
        spinbox.setValue(1)
        spinbox.setSingleStep(1)
        splint.numberWhoVoting.valueChanged.connect(spinbox.setValue)
        splint.voteButton.clicked.connect(self.voteFunction)
        splint.submitButton.clicked.connect(self.resultFunction)

    ##Function that determines what exactly happens when the vote button is pressed

    def voteFunction(self):
        print("run")
        choice1 = self.choice1

        choice2 = self.choice2

        choice3 = self.choice3
        nameInput = splint.voterNameInput
        names = self.names

        names.append(nameInput)
        print(nameInput)

        ##if self.ui.voteButton.isClicked():
        splint.numberWhoVoting = 1
        if splint.numberWhoVoting() == 1:
            choice1 += 1

        elif splint.numberWhoVoting() == 2:
            choice2 += 1

        elif splint.ui.numberWhoVoting() == 3:
            choice3 += 1

        else:
            pass

        ##self.ui.resultsSheet(set_text_content("VOTED!!!!!!"))
        print("voted")

        splint.resultsSheet.setText(f"VOTED!!!!!!!!")
        return choice1, choice2, choice3, names

    ##function that determines what happens when the submit button is clicked


    def resultFunction(self):
        print("RAN")
        choice1 = self.choice1
        choice2 = self.choice2
        choice3 = self.choice3
        names = self.names
        ##if self.ui.submitButton.isClicked():

        if choice1 > choice2 and choice1 > choice3:
                ##self.ui.resultsSheet(set_text_content("Choice 1 wins"))
            print("choice 1 wins")
            splint.resultsSheet.setText(f"Choice 1 wins")

        elif choice2 > choice1 and choice2 > choice3:
                ##self.ui.resultsSheet(set_text_content("Choice 2 wins"))
            print("choice 2 wins")
            splint.resultsSheet.setText(f"Choice 2 wins")

        elif choice3 > choice1 and choice3 > choice2:
                ##self.ui.resultsSheet(set_text_content("Choice 3 wins"))
            print("choice 3 wins")
            splint.resultsSheet.setText(f"Choice 3 wins")
        else:
                ##self.ui.resultsSheet(set_text_content("NOBODY WINS"))
            print("NOBODY WINS")
            splint.resultsSheet.setText(f"NOBODY WINS")
            ##self.ui.resultsSheet(set_text_content("names of those who voted" + names))
        print(f"names of those who voted {names}")
        splint.resultsSheet.setText(f"Names of those who voted {names}")







