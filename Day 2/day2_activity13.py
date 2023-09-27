sum = 0
count = 0

while True:
    number = input("Enter a number: ")

    if number.isnumeric():
        sum += float(number)
        count += 1
    else:
        print(f"The sum of {count} numbers is {sum}")
        break
