
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    
    def greet(self):
        print(f"Hello, my name is {self.name}.\nI am {self.age} years old.\nI live in {self.address}.\n")


joel = Person("Joel", 21, "North Palale, Tayabas City")
jaymark = Person("Jaymark", 17, "North Palale, Tayabas City")

joel.greet()
jaymark.greet()
