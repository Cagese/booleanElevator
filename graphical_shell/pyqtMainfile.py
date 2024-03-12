import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication,QMainWindow
from graphical_shell.ui import Ui_Boolean_Elevator
from classes import floors,elevators,peoples
class ElevatorGraphic(QMainWindow,Ui_Boolean_Elevator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setObjectName('test')
        self.simulation = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.mainThread)
        self.timer.start(10)

        self.testat = 0
        self.controlButton.clicked.connect(self.run)
        self.update_widgets()
    def run(self):
        if not(self.simulation):
            self.controlButton.setText('Остановить Симуляцию')
            [i.suspend_event.set() for i in elevators]
        else:
            self.controlButton.setText('Продолжить Симуляцию')
            [i.suspend_event.clear() for i in elevators]

        self.simulation = not self.simulation

    def update_widgets(self):
        self.departure1.setText(str(elevators[0].departure))
        self.departure2.setText(str(elevators[1].departure))
        self.departure3.setText(str(elevators[2].departure))
        self.departure4.setText(str(elevators[3].departure))
        self.searching1.setText(str(elevators[0].working))
        self.searching2.setText(str(elevators[1].working))
        self.searching3.setText(str(elevators[2].working))
        self.searching4.setText(str(elevators[3].working))
        self.people1.setText('\n'.join([i.queue[0] for i in elevators[0].people_in_cabine if i.queue]))
        self.people2.setText('\n'.join([i.queue[0] for i in elevators[1].people_in_cabine if i.queue]))
        self.people3.setText('\n'.join([i.queue[0] for i in elevators[2].people_in_cabine if i.queue]))
        self.people4.setText('\n'.join([i.queue[0] for i in elevators[3].people_in_cabine if i.queue]))
        self.levels_widget.setText('\n'.join([i.display_information()[0] for i in floors[::-1]]))
        self.elevators_widget.setText('\n'.join([i.display_information()[1] for i in floors[::-1]]))
        self.peoples_widgets.setText('\n'.join([i.display_information()[2] for i in floors[::-1]]))

    def mainThread(self):
        if self.simulation:
            temp = []
            for i in peoples:
                if i.queue:
                    if str(i.floor + 1) == i.queue[0]:
                        i.queue.pop(0)
                        if len(i.queue) == 0:
                            temp.append(i)
            while temp:
                peoples.remove(temp.pop(0))
            for i in floors:
                i.people = list(filter(lambda x:x.queue,i.people))
            for i in elevators:
                i.people_in_cabine =list(filter(lambda x:x.queue,i.people_in_cabine))
            #print([i.floor_count for i in floors if i.await_lift])
            #print([[i.people_in_cabine,i.working,i.departure] for i in elevators])
            #print([i for i in floors[2].people])
            if any([not i.working for i in elevators]):
                [i for i in filter(lambda x: x.working == False,elevators)][0].gotofloor([i.floor_count for i in sorted(filter(lambda x:x.await_lift==False,floors),key=lambda x:len(x.people),reverse=True)][0])
            [i.gotofloor(int(sorted(i.people_in_cabine,key=lambda x:int(x.queue[0]))[0].queue[0])) for i in elevators if i.people_in_cabine and i.departure and not i.working]

            if any([len(i.people)==0 for i in floors]) == 0:
                for i in elevators:
                    i.departure =True

        self.update_widgets()


def main():
    app = QApplication(sys.argv)
    ex = ElevatorGraphic()
    ex.show()
    sys.exit(app.exec_())
