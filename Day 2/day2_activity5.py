age = int(input("Enter your age: "))

if age >= 0 and age <= 12:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teen")
elif age >= 20 and age <= 64:
    print("Adult")
elif age > 64:
    print("Senior")
else:
    print("Invalid age input.")
