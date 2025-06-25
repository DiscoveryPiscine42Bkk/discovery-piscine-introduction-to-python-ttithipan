def array_of_names(persons):
    new_array = []
    for key, value in persons.items():
        new_array.append(key[0].upper()+ key[1:] + " " + value[0].upper() + value[1:])
    return new_array

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))