#!/usr/bin/env python3

with open("verhaal.txt") as f:
    regels = f.readlines()

regels.reverse() # of: regels = regels[::−1]

for regel in regels:
    print(regel, end='')
