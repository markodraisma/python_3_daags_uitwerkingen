def gemiddelde(lijst):
    lijst = lijst[:]
    som = sum(lijst)
    aantal = len(lijst)
    resultaat = som/aantal
    return resultaat


def gemiddelde2(lijst):
    lijst = lijst[:]
    som = sum(lijst)
    aantal = len(lijst)
    gem = som/aantal
    return  gem, aantal

getallen = [ 1, 5, 2, 33, 5, 16, 7 ]

print("het gemiddelde van de", len(getallen), \
      "items in", getallen, "is:", gemiddelde(getallen))

avg, count = gemiddelde2(getallen)
print("het gemiddelde van de %d items in %s is: %.2f" % (
       count, getallen , avg ))

