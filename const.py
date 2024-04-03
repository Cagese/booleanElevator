with open('const.txt') as file:
    settings = list(map(lambda x:float(x.strip()),file.readlines()))

debug = settings[0]
t_elev_movmement = settings[1] * debug
t_elev_doors_movment = settings[2] * debug
t_people_boarding = settings[3] * debug
max_people_in_cabine = settings[4]
colors = ['#2C69A9','#6B6B6B','#C47D00','#690B6F']



