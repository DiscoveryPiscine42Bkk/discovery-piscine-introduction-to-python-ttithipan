#!/usr/bin/env python3
number = input("Enter a number:\n")
try:
    number = int(number)
    for i in range(1, 10):
        print(i, "X", number, "=", number * i)
except ValueError:
    raise ValueError("Error: Please enter a valid integer.")