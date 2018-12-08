places = ["New York", "Paris", "Rome", "Tokyo"]

print("Look at this list:\n")
for place in places:
    print(place)

new_place = input("Tell me a similar place:\n")
places.append(new_place)

print("Look at the new list:\n")
for place in places:
    print(place)
    