#!/usr/bin/env python3
number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")
try:
    number1, number2 = int(number1), int(number2)
    result = number1 * number2
    print(number1, "X", number2, "=", result)
    if result == 0:
        print("The result is positive and negative.")
    elif result < 0:
        print("The result is negative.")
    else:
        print("The result is positive.")
except:
    raise ValueError
