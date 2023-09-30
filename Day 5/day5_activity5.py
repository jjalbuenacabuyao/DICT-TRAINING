
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species


    def speak(self):
        print(f"{self.name} is an {self.species} and makes a sound.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed


    def speak(self):
        print(f"{self.name} is a {self.breed} dog barks.")


class Cat(Animal):
    def __init__(self, name, color, breed):
        super().__init__(name, species="Cat")
        self.color = color
        self.breed = breed


    def speak(self):
        print(f"{self.name} is a {self.color} cat meows.")


milkshake = Dog("Milkshake", "ASPIN")
ming = Cat("Ming", "orange", "PUSPIN")

milkshake.speak()
ming.speak()
