import sys
if len(sys.argv) < 3:  # Check if there are no command line arguments
    print("none")  # Print "none" if no arguments are provided
else:
    for index in range(len(sys.argv)-1, 0, -1):  # Iterate from the last argument to the first
        print(sys.argv[index],end=" ")
    