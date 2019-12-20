uurwaarden = "673,1449,82,100019341,13,996308,53,7,4711,2,189320"

uurwaarden = uurwaarden.split(",")
totaal = 0

# eerst de breedte van het grootste getal bepalen:
# het totaal van alle uren

for uur in uurwaarden:
    totaal+=int(uur)

lengte = len(str(totaal))

# nu de gevonde lengte (7) gebruiken 
# om de variabele melding mee samen te stellen:

# melding = "Uur %%2d: %%%dd" % lengte      # resultaat: "Uur %2d: %7d"
# print("DEBUG - melding is nu:", melding)  # even controleren of het klopt

# nu de melding gebruiken bij het printen van de uren in nette kolommen:

for nr, uur in enumerate(uurwaarden):
    uur = int(uur)
#    print(melding % (nr+1, uur))
    print("Uur %2d: %*d" % (nr+1, lengte, uur))
	
print("Totaal:", totaal)
