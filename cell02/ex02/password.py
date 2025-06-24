password = "Python is awesome"
input = input("Enter the password: ")
if input == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
    raise ValueError("Wrong password")

