party_size = input("How many people are in your dinner group? ")
party_size = int(party_size)

if party_size > 8:
    print("I'm sorry, you will have to wait for the next table.")
else:
    print("Your table is ready.")