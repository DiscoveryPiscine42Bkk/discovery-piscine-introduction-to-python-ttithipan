import sys
text = sys.argv[1] if len(sys.argv) > 1 else ""
if len(text) == 0:
    print("None")
else:
    for i in text:
        if i == "z":
            print("z", end="")
print()


