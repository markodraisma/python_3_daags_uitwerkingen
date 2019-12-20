#!/usr/bin/env python3

# tabel karakters

for i in range(128):
    print(i, oct(i), hex(i), end = ' ')
    if 32 <= i <= 126:
        print(chr(i))
    else:
        print()

print()
for i in range(128):
    if str(chr(i)).isprintable():
        print(i, oct(i), hex(i), chr(i))
    else:
        print(i, oct(i), hex(i))
