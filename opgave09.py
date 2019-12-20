try:
    f = open("weer.txt")
except Exception:
    import sys
    sys.exit("Foutje")

steden = {}
for regel in f:
    if regel[0] == '#':
        continue
    regel = regel.rsplit(" ", 1)
    try:
        temp = float(regel[-1])
    except Exception:
        continue
    stad = regel[0]
    steden[stad]=temp

gemiddeld = sum(steden.values()) / len(steden)
print("gemiddelde temperatuur:", gemiddeld)

laag = {}
hoog = {}
for stad in steden:
    temp = steden[stad]
    if temp<gemiddeld:
        laag[stad] = temp
    else:
        hoog[stad] = temp


print("\nsteden onder het gemiddelde:")
for stad, temp in sorted(laag.items()):
    print("{}: {}".format(stad, temp))
print("\nsteden boven of op het gemiddelde:")
for stad, temp in sorted(hoog.items()):
    print("{}: {}".format(stad, temp))

f.close()

