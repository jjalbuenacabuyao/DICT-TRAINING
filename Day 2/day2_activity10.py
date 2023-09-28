max = int(input("Enter the max number of *: "))

for i in range(1, max + 1):
    print("*" * i)
    if i == max:
        for j in range(max - 1, 0, -1):
            print("*" * j)
