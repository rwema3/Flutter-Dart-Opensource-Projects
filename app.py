import os
from random import randint

for i in range(1, 1200):

    for j in range(0, randint(1, 20)):
        d = str(i) + ' days ago'
        with open('file.text', 'a') as file:
            file.write(d)
        os.system('git add .')
