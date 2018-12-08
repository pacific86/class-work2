def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    # Build a new list to hold the great musicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)

magicians = ['Houdini', 'David Copperfield', 'Criss Angel']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)