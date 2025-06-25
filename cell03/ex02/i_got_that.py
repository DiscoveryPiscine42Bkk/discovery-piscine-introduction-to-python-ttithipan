#!/usr/bin/env python3
print("What you gotta say? : ", end='')
input_text = input()
while True:
    if input_text == "STOP":
        break
    else: 
        print("I got that! Anything else? : ", end='')
    input_text = input()
