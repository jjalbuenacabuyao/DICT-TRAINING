firstname = input("Enter your firstname: ")
middlename = input("Enter your middle name: ")
lastname = input("Enter your lastname: ")

name = f"{firstname} {middlename} {lastname}".title()

for character in name:
    print(character)

print(name[2:10])

splitted_value = name.split(" ")
for item in splitted_value:
    print(item)

for character in range(len(name)):
    print(name[character], end="")