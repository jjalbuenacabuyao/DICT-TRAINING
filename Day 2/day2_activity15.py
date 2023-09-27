fruits = ["banana", "oranges", "apples", "mangoteen"]
fruits.append("grapes")
fruits.append("strawberry")
fruits.pop()
fruits.sort()
selected_fruits = fruits[1:3]
selected_fruit = fruits[2]
selected_fruits_2 = fruits[2:]

for fruit in fruits:
    print(fruit)