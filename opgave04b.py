#!/usr/bin/env python3

uurwaarden = "673,1499,82,119341,13,996308,53,7"
uren = uurwaarden.split(’,’)
tot = 0

for num, getal in enumerate(uren):
    print("Uur ", str(num+1) + ":", getal)
    tot += int(getal)

print("Totaal:", tot)
