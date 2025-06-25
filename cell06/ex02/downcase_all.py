import sys
def downcase_it(string):
    return string.lower()
if len(sys.argv) > 1:
    print(downcase_it(sys.argv[1]))
    print("I understood arrays well!")
else:
    print("None")
    