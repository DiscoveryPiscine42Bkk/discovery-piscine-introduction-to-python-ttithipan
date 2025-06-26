import sys
new_list = []
if len(sys.argv) != 3 :
    print("None")
else:    
    for number in range(int(sys.argv[1]), int(sys.argv[2])+1):
        new_list.append(number)
    print(new_list)