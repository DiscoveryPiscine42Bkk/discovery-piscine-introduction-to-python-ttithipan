#!/usr/bin/env python3
number = input("Give me a number: ")
try:
    number = int(number)
    print(f"{number} is an integer.")
except:
    print(f"{number} is a decimal.")