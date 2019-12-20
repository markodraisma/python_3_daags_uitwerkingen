#!/usr/bin/env python3
with open("woorden.txt") as f:
    lijst = [ regel[::-1] for regel in f ]

# print(lijst)
# lijst = []
# for regel in f:
#     lijst.append( regel[::-1] )

lijst.sort()

for regel in lijst:
    regel = regel.lstrip()
    print(regel[::-1])

