import os

inp = open(os.path.normpath('de.dic'), 'r')
lines = inp.readlines()

for line in lines:
    if len(line) <= 4:
        print(line)