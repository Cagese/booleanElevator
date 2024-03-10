import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication,QMainWindow
from .ui import Ui_MainWindow
from classes import floors,elevators
class ElevatorGraphic(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.simulation = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.mainThread)
        self.timer.start(10)

        self.testat = 0
        self.controlButton.clicked.connect(self.run)
        self.outputWidget.setText('\n'.join([i.__repr__() for i in floors][::-1]))
    def run(self):
        if not(self.simulation):
            self.controlButton.setText('Остоновить Симуляцию')
        else:
            self.controlButton.setText('Начать Симуляцию')


        self.simulation = not self.simulation

    def mainThread(self):
        if self.simulation:
            if self.testat==0:
                self.testat+=1
                elevators[0].gotofloor(10)
                elevators[1].gotofloor(30)
        self.outputWidget.setText('\n'.join([i.__repr__() for i in floors][::-1]))

def main():
    app = QApplication(sys.argv)
    ex = ElevatorGraphic()
    ex.show()
    sys.exit(app.exec_())
