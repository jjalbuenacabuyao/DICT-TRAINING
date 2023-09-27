num = int(input("Enter number of columns: "))

for col in range(1, num + 1):
    for row in range(1, num + 1):
        print(row * col, end="\t")
    print()
