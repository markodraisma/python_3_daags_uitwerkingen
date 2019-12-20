import os
import sys
from os.path import join, getsize

tellers = [0] * 10

for root, dirs, files in os.walk(sys.argv[1]):
    for name in files:
        try:
            pathname = join(root, name)
            grootte = getsize(pathname)
            cijfer = int(str(grootte)[0])
            tellers[cijfer] += 1
        except Exception:
            pass

totaal = sum(tellers[1:])

for cijfer in range(1,10):
    print("{:d}: {:6.2%}".format(cijfer, tellers[cijfer]/totaal))
