guests = ['Victor Hugo', 'Michelle Obama', 'Adele']
print(" You are invited to my dinner party, " + guests[0] + ".")
print(" You are invited to my dinner party, " + guests[1] + ".")
print(" You are invited to my dinner party, " + guests[2] + ".")

print(" Unfortunately Victor Hugo cannot attend.")

oldguest = guests.pop(1)
guests.insert(0,'John Legend')

print(" You are invited to my dinner party, " + guests[0] + " instead of Victor Hugo.")

print(" You are invited to my dinner party, " + guests[0] + ".")
print(" You are invited to my dinner party, " + guests[1] + ".")
print(" You are invited to my dinner party, " + guests[2] + ".")