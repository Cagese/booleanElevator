import csv
from classes import floors,people

def import_from_csv(filename):
    with open(filename,encoding='utf8') as csvfile:
        data = list(csv.reader(csvfile,delimiter=',',quotechar='"'))
    for i in data[1:]:
        floors[int(i[0])-1].add_peoples([people(i[1].split())])