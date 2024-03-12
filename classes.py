from threading import Thread, Event
from time import sleep
from const import *


class floor:
    def __init__(self, floor_level, people=None):
        if people is None:
            people = []
        self.people = people
        self.elevators = []
        self.floor_count = int(floor_level)
        self.await_lift = False

    def add_peoples(self, peoples):
        [self.people.append(i) for i in peoples]

    def display_information(self):
        return [f'Этаж {self.floor_count}',
                f"Лифты: {' '.join(map(lambda x: x.__repr__(), sorted(self.elevators, key=lambda x: x.number)))}",
                f"Люди: {' '.join(map(lambda x: x.__repr__(), self.people))}"]


class people:
    def __init__(self, floor, queue=None, ):
        peoples.append(self)
        if queue is None:
            queue = [0]
        self.queue = queue
        self.floor = floor

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
        self.suspend_event = Event()
        self.working = False
        self.departure = False

    def gotofloor(self, floor_level):

        self.working = True
        floors[floor_level - 1].await_lift = True

        def thread(floor_level):
            if floor_level == self.floor.floor_count or len(self.people_in_cabine) >= 10:
                self.departure = True
            if self.floor.floor_count > floor_level:
                for i in range(self.floor.floor_count, floor_level, -1):
                    unloading_people(i)
                    for j in self.floor.people:
                        if j.queue:
                            if i >= int(j.queue[0]) >= floor_level:
                                self.people_in_cabine.append(self.floor.people.pop(self.floor.people.index(j)))
                    else:
                        sleep(t_people_boarding)

                    step_movment(i, -2)
            else:
                for i in range(self.floor.floor_count, floor_level):
                    unloading_people(i)
                    for j in self.floor.people:
                        if j.queue:
                            if i <= int(j.queue[0]) <= floor_level:
                                self.people_in_cabine.append(self.floor.people.pop(self.floor.people.index(j)))
                    else:
                        sleep(t_people_boarding)

                    step_movment(i, 0)
            if self.floor.people:
                self.people_in_cabine.append(self.floor.people.pop(0))
            floors[floor_level - 1].await_lift = False
            self.working = False

        if self.departure:
            if self.floor.people:
                self.people_in_cabine.append(self.floor.people.pop(0))

        def unloading_people(i):
            if any([j.queue[0] == str(i) for j in self.people_in_cabine if j.queue]):
                for j in self.people_in_cabine:
                    if j.queue:
                        if j.queue[0] == str(i):
                            del j.queue[0]
                            self.floor.people.append(self.people_in_cabine.pop(self.people_in_cabine.index(j)))

        def step_movment(i, shift):
            self.suspend_event.wait()
            del self.floor.elevators[self.floor.elevators.index(self)]
            self.floor = floors[i + shift]
            self.floor.elevators.append(self)
            sleep(t_elev_movmement)

        th = Thread(target=thread, args=(floor_level,), daemon=True)
        th.start()

    def __repr__(self):
        return self.number


peoples = []
floors = [floor(i + 1) for i in range(40)]
elevators = [elevator(i + 1) for i in range(4)]
