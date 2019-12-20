#!/usr/bin/env python3
# Mogelijkheid I: open file als ’text’
f = open("limerick.txt", encoding="utf−8")
rcount = 0 # regel teller
wcount = 0 # woorden teller
ccount = 0 # character teller
bcount = 0 # bytes teller

for regel in f:
    rcount += 1
    wcount += len(regel.split())
    ccount += len(regel)
    # converteer string naar bytes en bepaal lengte
    bcount += len( regel.encode('utf−8') )

print(rcount, wcount, ccount, bcount)
f.close()
