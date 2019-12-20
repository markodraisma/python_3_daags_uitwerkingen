f = open("verhaal.txt")

woorden = {}
woordenlijst = {}
i = 1
for regel in f:
    regel = regel.rstrip().lower()
    #regel = tekens.split(regel)
    regel = regel.split()
    for woord in regel:
        woord = woord.strip(" ,.;:!'\"")
        woorden[woord] = woorden.setdefault(woord,0)+1
        woordenlijst.setdefault(woord,[])
    #    if not i in woordenlijst[woord]:
        woordenlijst[woord].append(i)
    i+=1
        
print("woord frequenties:")
for woord in sorted(woorden, key=lambda x: "{:04}{}".format(100-woorden[x],x)):
    print(woord, woorden[woord])

print("\nin de volgende regels...")
for woord in sorted(woordenlijst):
    print(woord, woordenlijst[woord])
