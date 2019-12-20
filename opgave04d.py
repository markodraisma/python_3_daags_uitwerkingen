uurwaarden = "673,1449,82,119341,13,996308,53,7,4711,2,189320"

uurwaarden = uurwaarden.split(",")
totaal = 0
for nr, uur in enumerate(uurwaarden):
    uur = int(uur)
    melding = "Uur {:2d}: {:7d}".format(nr+1, uur)
    print(melding)
    totaal += uur
print("Totaal:", totaal)
