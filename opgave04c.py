uurwaarden = "673,1449,82,119341,13,996308,53,7,4711,2,189320"

uurwaarden = uurwaarden.split(",")
for index, uur in enumerate(uurwaarden):
    uurwaarden[index] = int(uur)
    
# of: uurwaarden = list(map(int,uurwaarden))

totaal = sum(uurwaarden)

for nr, uur in enumerate(uurwaarden):
   # uur = int(uur)
    melding = "Uur %2d: %7d" % (nr + 1, uur)
    print(melding)
#   totaal += uur
print("Totaal:", totaal)
