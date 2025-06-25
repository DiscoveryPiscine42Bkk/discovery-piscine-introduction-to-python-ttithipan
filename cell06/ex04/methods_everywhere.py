import sys
def shrink(input_string):
    return input_string[0:8]
def enlarge(input_string):
    return input_string + (8-len(input_string))*"Z"

for arg in sys.argv[1:]:
    if len(arg) < 8:
        print(enlarge(arg))
    elif len(arg) > 8:
        print(shrink(arg))
    else:
        print(arg)