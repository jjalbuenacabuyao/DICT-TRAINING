
class Car:
    def __init__(self, make, model, year, engine_size):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0
        self.engine_size = engine_size

    
    def accelerate(self):
        self.speed = (self.engine_size) * 1200

    
    def update_model(self, new_model):
        self.model = new_model

    def brake(self):
        self.speed -= 10


my_car = Car("Hello", "World", 2023, 1.5)

print(my_car.model)
my_car.accelerate()
my_car.accelerate()
my_car.brake()
my_car.update_model("QWERTY")
print(my_car.model)