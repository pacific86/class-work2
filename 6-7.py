# Make an empty list to store people in.
people = []

# Define some people, and add them to the list.
person = {
    'first_name': 'austin',
    'last_name': 'breedveld',
    'age': 36,
    'city': 'phoenix',
    }
people.append(person)

person = {
    'first_name': 'liz',
    'last_name': 'oxenrider',
    'age': 33,
    'city': 'modesto',
    }
people.append(person)

person = {
    'first_name': 'marianne',
    'last_name': 'ammendolia',
    'age': 65,
    'city': 'patterson',
    }
people.append(person)

# Display all of the information in the dictionary.
for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()
    
    print(name + ", of " + city + ", is " + age + " years old.")