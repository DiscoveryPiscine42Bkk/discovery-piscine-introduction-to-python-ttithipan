def greetings(person = "Noble Stranger"):
    try:
        int(person)
        print("Error! It was not a name.")
    except:
        print(f"Hello, {person}!")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
