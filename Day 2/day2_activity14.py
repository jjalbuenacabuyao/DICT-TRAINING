odd = ""
even = ""
odd_number_count = 0
even_number_count = 0

for i in range(1, 11):
    number = int(input(f"Enter #{i}: "))

    if number % 2 == 0:
        even += str(number) + ", "
        even_number_count += 1
    elif number % 2 != 0:
        odd += str(number) + ", "
        odd_number_count += 1
    else:
        print("Invalid input")

print(f"There are {odd_number_count} ODD numbers - {odd}")
print(f"There are {even_number_count} even numbers - {even}")
