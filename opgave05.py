#!/usr/bin/env python3
 
getallen=[ 1, 5, 2, 33, 5, 16, 7 ]
 
# Voeg hieronder je code toe die het gemiddelde uitrekent.

totaal = sum(getallen)
aantal = len(getallen)
gemiddeld = totaal / aantal;

print("Gemiddelde: ", gemiddeld)
print("Dat is afgerond: ", round(gemiddeld, 2))
print("Dat is ook afgerond: %.2f" % gemiddeld)
