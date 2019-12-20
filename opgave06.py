#!/usr/bin/ens python3

# opgave 6 a
"""
basis=2
n = 1
for i in range (1,1001):
    n *= basis  
    print(n)
print()

# opgave 6 b

tellers = [0 for i in range(10) ]
tellers = [0] * 10

for i in range(1,1001):
    x = 2 ** i
    begincijfer = int(str(x)[0])
    tellers[begincijfer]+=1

print("Frequentie van begincijfers machten van 2:", tellers)
print()
"""

for basis in range(2,21):
    tellers = [0]*10
    n = 1
    for x in range(1,10001):
        n*=basis               # levert op: basis tot de macht x
        cijfer=int(str(n)[0])  # wat is daarvan het eerste cijfer?
        tellers[cijfer]+=1     # hoog element met die index op
    print(basis, ":", tellers[1:]) # getallen beginnen niet met 0  
        
