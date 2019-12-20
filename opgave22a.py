#!/usr/bin/env python3

import os
import sys
from os.path import join, getsize

for root, dirs, files in os.walk(sys.argv[1]):
    for name in files:
        try:
            pathname = join(root, name)
            grootte = getsize(pathname)
            print("{:25}: {:10d}".format(pathname, grootte))
        except Exception:
            pass
