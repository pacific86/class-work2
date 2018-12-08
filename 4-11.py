pizzas = ["cheese", "sausage", "pepperoni", "olive"]
friends_pizzas = pizzas[:]

pizzas.append("pineapple")
friends_pizzas.append("onion")
    
for pizza in pizzas:
    print("My favorite pizzas are " + pizza + ".")
    
for pizza in friends_pizzas:
    print("My friend's favorite pizzas are " + pizza + ".")