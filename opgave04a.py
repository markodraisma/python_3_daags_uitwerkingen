#!/usr/bin/env python3
#
# aantal 5 in 2 ** 1000

getal = 2 ** 1000
getal = str(getal)

# eenvoudige versie:
print("Er zitten", getal.count('5'), "cijfers 5 in", getal)

# waarom makkelijk doen als het ook moeilijk kan?
lengte = len(getal)
lengte_zonder_5 = len(getal.replace('5',''))
print("Er zitten",lengte-lengte_zonder_5,"cijfers 5 in", getal)
