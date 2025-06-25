# your method definition here
def find_the_redheads(family):
    redheads = []
    for member, hair_color in family.items():
        if hair_color == "red":
            redheads.append(member)
    return redheads


dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))
