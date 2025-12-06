my_pizzas = ["Margherita Pizza", "Pepperoni Pizza", "Veg Extravaganza"]

friends_pizzas = my_pizzas[:]

my_pizzas.append("Schezwan Pizza")
friends_pizzas.append("Paneer Chilli Pizza")

print("My Pizzas:")
for pizza in my_pizzas:
    print(pizza)

print("Friend's Pizzas:")
for pizza in friends_pizzas:
    print(pizza)
