from random import randint
from pprint import pprint
for i in range(30):
    print(f'{randint(1,1)},',end='')
    for j in range(randint(2,3)):
        print(randint(1,40),end=' ')
    print(' ')
