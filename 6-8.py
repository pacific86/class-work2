# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'pit bull',
    'name': 'charlotte',
    'owner': 'janelle',
    'weight': 72,
    'eats': 'dog food',
}
pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'chaz',
    'owner': 'jeff',
    'weight': 12,
    'eats': 'cat food',
}
pets.append(pet)

pet = {
    'animal type': 'turtle',
    'name': 'charlie',
    'owner': 'marriane',
    'weight': 2,
    'eats': 'leaves',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))