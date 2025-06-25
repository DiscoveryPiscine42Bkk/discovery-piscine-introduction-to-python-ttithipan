import sys
input_string = sys.argv[1] if len(sys.argv) > 1 else ""
answer = input("What was the parameter? : ")
if input_string == answer:
    print("Good job!")
else:
    print("Nope, sorry...")
