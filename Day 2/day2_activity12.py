count = 0

while True:
    name = input("Enter a name: ")

    if name == "stop":
        print(f"Loop ran {count} times")
        break
