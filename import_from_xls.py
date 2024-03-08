import csv
from classes import floors,people

def import_from_xls(filename):
    with open(filename,encoding='utf8') as csvfile:
        data = list(csv.reader(csvfile,delimiter=',',quotechar='"'))
    for i in data[1:]:
        floors[int(i[0])].add_peoples([people(i[1].split())])