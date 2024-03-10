from threading import Thread
from time import sleep
from const import *


class floor:
    def __init__(self, floor_level, people=None):
        if people is None:
            people = []
        self.people = people
        self.elevators = []
        self.floor_count = int(floor_level)

    def add_peoples(self, peoples):
        [self.people.append(i) for i in peoples]

    def __repr__(self):
        return f'''Этаж {self.floor_count}\t Лифты: {' '.join(map(lambda x: x.__repr__(), sorted(self.elevators,key=lambda x:x.number)))}\t Люди: {' '.join(map(lambda x: x.__repr__(), self.people))}'''

class people:
    def __init__(self, queue=None):
        peoples.append(self)
        if queue is None:
            queue = [0]
        self.queue = queue

    def __repr__(self):
        if self.queue:
            return str(self.queue[0])
        else:
            return 'noQ'


class elevator:
    def __init__(self, number):
        floors[0].elevators.append(self)
        self.floor = floors[0]
        self.people_in_cabine = []
        self.number = f'№{number}'

    def gotofloor(self, floor_level):

        def thread(floor_level):
            for i in range(floor_level):
                del self.floor.elevators[self.floor.elevators.index(self)]
                self.floor = floors[i]
                self.floor.elevators.append(self)
                sleep(t_elev_movmement)

        th = Thread(target=thread,args=(floor_level,),daemon=True)
        th.start()

    def __repr__(self):
        return self.number

peoples = []
floors = [floor(i + 1) for i in range(40)]
elevators = [elevator(i + 1) for i in range(4)]
