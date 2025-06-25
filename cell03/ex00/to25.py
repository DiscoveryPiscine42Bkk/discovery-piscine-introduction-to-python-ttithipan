#!/usr/bin/env python3
number = input("Enter a number less than 25\n")
try:
    number = int(number)
    if number < 25:
        while number <= 25:
            print("Inside the loop, my variable is", number)
            number += 1
    else:
        print("Error")
except:
    raise ValueError("Error")