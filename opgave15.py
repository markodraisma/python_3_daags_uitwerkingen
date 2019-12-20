#!/usr/bin/env python3
def fibo(maxval):
    """
    Fibonacci sequence generator
    argument:
    maxval − generated values must be smaller
    """
    prev = 1
    cur = 0
    while cur < maxval:
        yield cur
        prev, cur = cur, cur+prev
    return

for val in fibo(1000):
    print(val)
