from pprint import pprint

class floor:
    def __init__(self, floor_level, people=None):
        if people is None:
            people = []
        self.people = people
        self.floor_count = int(floor_level)

    def add_peoples(self, peoples):
        [self.people.append(i) for i in peoples]

    def __repr__(self):
        return ' '.join(map(lambda x: x.__repr__(), self.people))


floors = [floor(i + 1) for i in range(40)]


class people:
    def __init__(self, queue=None):
        if queue is None:
            queue = [0]
        self.queue = queue

    def __repr__(self):
        return str(self.queue[0])


class elevator:
    def __init__(self):
        self.floor = floors[0]


floors[2].add_peoples([people(queue=[1, 3, 5]),people(queue=[2, 3, 5]),people(queue=[3, 5])])
floors[1].add_peoples([people(queue=[6]),people(queue=[5]),people(queue=[3])])

pprint(floors)
