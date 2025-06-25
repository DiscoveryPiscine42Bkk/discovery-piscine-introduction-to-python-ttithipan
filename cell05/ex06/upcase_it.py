import sys
if len(sys.argv) < 2:  # Check if there are no command line arguments
    print("none")  # Print "none" if no arguments are provided
else:
    args = sys.argv[1] #Get the first argument after the script name
    print(args.upper())
    

