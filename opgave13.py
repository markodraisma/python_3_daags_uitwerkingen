#!/usr/bin/env python3

def dubbelen(l_namen):
    l_namen = l_namen[:]
    l_dubbelen = []
    for idx in range(1,len(l_namen)):
        naam = l_namen[idx]
        if idx > l_namen.index(naam):
            l_dubbelen.append(idx)
    return tuple(l_dubbelen)

def dubbelen2(l_namen):
    l_namen = l_namen[:]
    l_gevonden = []
    l_dubbelen = []
    for i, naam in enumerate(l_namen):
        if naam in l_gevonden:
            l_dubbelen.append(i)
        else:
            l_gevonden.append(naam)
    return tuple(l_dubbelen)

namen = [ 'jan', 'piet', 'henk', 'els', 'piet',
          'els', 'john', 'els', 'jan', 'els', 'henk']

# namen.sort()

print("De invoerlijst wordt:", namen)

dublist = dubbelen(namen)

print(dublist)

dublist = dubbelen2(namen)

print(dublist)


