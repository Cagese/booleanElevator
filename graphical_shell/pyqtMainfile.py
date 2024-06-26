import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from graphical_shell.ui import Ui_Boolean_Elevator
from classes import floors, elevators, peoples
from const import debug
from PyQt5 import QtCore, QtWidgets

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

colors = {True: '#166F0B', False: '#6C0000'}

class ElevatorGraphic(QMainWindow, Ui_Boolean_Elevator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setObjectName('test')
        self.simulation = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.mainThread)
        self.stopwatch_timer = QTimer()
        self.stopwatch_timer.timeout.connect(self.stopwatch_update)
        self.timer.start(10)
        self.stopwatch_start = 0
        self.custom_algoritm = True

        self.controlButton.clicked.connect(self.run)
        self.update_widgets()
        self.lift1name.setText(f'<a style="color:#2C69A9"> {self.lift1name.text()} </a>')
        self.lift2name.setText(f'<a style="color:#6B6B6B"> {self.lift2name.text()} </a>')
        self.lift3name.setText(f'<a style="color:#C47D00"> {self.lift3name.text()} </a>')
        self.lift4name.setText(f'<a style="color:#690B6F"> {self.lift4name.text()} </a>')



    def stopwatch_update(self):
        self.stopwatch_start += 1
        print(self.stopwatch_start)

    def run(self):
        if not (self.simulation):
            self.stopwatch_timer.start(int(1000 * debug))
            self.controlButton.setText('Остановить Симуляцию')
            [i.suspend_event.set() for i in elevators]
        else:
            self.stopwatch_timer.stop()
            self.controlButton.setText('Продолжить Симуляцию')
            [i.suspend_event.clear() for i in elevators]

        self.simulation = not self.simulation

    def update_widgets(self):
        self.departure1.setText(f'<a style="color: {colors[elevators[0].departure]}">{str(elevators[0].departure)}</a>')
        self.departure2.setText(f'<a style="color: {colors[elevators[1].departure]}">{str(elevators[1].departure)}</a>')
        self.departure3.setText(f'<a style="color: {colors[elevators[2].departure]}">{str(elevators[2].departure)}</a>')
        self.departure4.setText(f'<a style="color: {colors[elevators[3].departure]}">{str(elevators[3].departure)}</a>')
        self.searching1.setText(f'<a style="color: {colors[elevators[0].working]}">{str(elevators[0].working)}</a>')
        self.searching2.setText(f'<a style="color: {colors[elevators[1].working]}">{str(elevators[1].working)}</a>')
        self.searching3.setText(f'<a style="color: {colors[elevators[2].working]}">{str(elevators[2].working)}</a>')
        self.searching4.setText(f'<a style="color: {colors[elevators[3].working]}">{str(elevators[3].working)}</a>')
        self.people1.setText('\n'.join([i.queue[0] for i in elevators[0].people_in_cabine if i.queue]))
        self.people2.setText('\n'.join([i.queue[0] for i in elevators[1].people_in_cabine if i.queue]))
        self.people3.setText('\n'.join([i.queue[0] for i in elevators[2].people_in_cabine if i.queue]))
        self.people4.setText('\n'.join([i.queue[0] for i in elevators[3].people_in_cabine if i.queue]))
        self.levels_widget.setText('<p style="line-height: 0.1;">' + '<p style="line-height: 0.1;">'.join(
            [i.display_information()[0] for i in floors[::-1]]))
        self.elevators_widget.setText('<p style="line-height: 0.1;">' + '<p style="line-height: 0.1;">'.join(
            [i.display_information()[1] for i in floors[::-1]]))
        self.peoples_widgets.setText('<p style="line-height: 0.1;">' + '<p style="line-height: 0.1;">'.join(
            [i.display_information()[2] for i in floors[::-1]]))

    def mainThread(self):
        if self.simulation:

            for i in elevators:
                i.custom_algoritm = self.custom_algoritm
            for i in floors:
                i.people = list(filter(lambda x: x.queue, i.people))
            for i in elevators:
                i.people_in_cabine = list(filter(lambda x: x.queue, i.people_in_cabine))

            if self.custom_algoritm:
                stack = [i for i in
                         filter(lambda x: x.working == False and x.departure == False and len(x.people_in_cabine) == 0,
                                elevators)]
                if len(stack):
                    stack[0].gotofloor(
                        [i.floor_count for i in
                         sorted(filter(lambda x: x.await_lift == False, floors), key=lambda x: len(x.people),
                                reverse=True)][0])

                [i.gotofloor(int(sorted(i.people_in_cabine, key=lambda x: int(x.queue[0]))[0].queue[0])) for i in
                 elevators
                 if i.people_in_cabine and not i.working]

                if any([len(i.people) != 0 for i in floors]) == 0 or all([len(i.people_in_cabine) for i in elevators]):
                    for i in elevators:
                        i.departure = True
            else:
                stack = [i for i in
                         filter(lambda x: x.departure == False and len(x.people_in_cabine) <= 7 and x.working == False,
                                elevators)]
                if len(stack):
                    if [i.floor_count for i in
                        filter(lambda x: x.people, floors)]:
                        stack[0].gotofloor(
                            [i.floor_count for i in
                             filter(lambda x: x.people, floors)][0])
                for i in filter(lambda x: x.working == False, elevators):
                    if i.departure:
                        people_in_cabine = sorted(i.people_in_cabine, key=lambda x: int(x.queue[0]), reverse=True)
                        if people_in_cabine:
                            i.gotofloor(int(people_in_cabine[0].queue[0]))

                for i in elevators:
                    if not (len(i.people_in_cabine) <= 7) or any([len(i.people) != 0 for i in floors]) == 0 or all(
                            [len(i.people_in_cabine) for i in elevators]):
                        i.departure = True

            if all([len(i.people) == 0 for i in floors]) and all([len(i.people_in_cabine) == 0 for i in elevators]):
                self.stopwatch_timer.stop()
        self.update_widgets()


def main():
    app = QApplication(sys.argv)
    ex = ElevatorGraphic()
    ex.show()
    sys.exit(app.exec_())
