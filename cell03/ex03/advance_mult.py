#!/usr/bin/env python3
import sys
if len(sys.argv) !=1:
    print("None")
else:
    x = 0
    y = 0
    while x < 11:
        print(f"Table de {x}:", end=" ")
        while y < 11:
            print(x*y, end=" ")
            y += 1
        y = 0
        print("")
        x += 1

