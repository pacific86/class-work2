foods = ["cannoli", "pizza", "calzone", "salad"]
friends_foods = foods[:]

foods.append("calamari")
friends_foods.append("bruschetta")
    
for food in foods:
    print("My favorite menu items are " + food + ".")
    
for food in friends_foods:
    print("My friend's favorite menu items are " + food + ".")