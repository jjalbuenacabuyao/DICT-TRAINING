fruits = []

while True:
    input_fruit = input("Enter the name of the fruit: ")

    if input_fruit in fruits:
        print("Fruit already exist in the list")
    elif input_fruit.lower() == "stop":
        print("Loop terminated")
        break
    else: 
        fruits.append(input_fruit)
        print("Fruit added to the list")

print("Fruit entered: ", fruits)
