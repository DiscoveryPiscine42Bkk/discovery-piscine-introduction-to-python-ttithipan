#!/usr/bin/env python3
input_string = input()
for char in input_string:
    if char.isupper():
        print(char.lower(), end="")
    elif char.islower():
        print(char.upper(), end="")
    else:
        print(char, end="")
print()  # Print a newline at the end