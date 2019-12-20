#!/usr/bin/env python3

filename = 'verhaal.txt'

try:
    f = open(filename,'r')
except Exception:
    import system
    print('File %s not found!' % filename)
    system.exit()

nr_of_lines = 0
nr_of_words = 0
nr_of_chars = 0

print()

for line in f:
    print(line.rstrip())
    nr_of_lines += 1
    words = line.split()
    nr_of_words += len(words)
    nr_of_chars += len(line)

print('\nFile %s has %d lines, %d words, %d characters' % \
        (filename, nr_of_lines, nr_of_words, nr_of_chars))    
f.close()
