import random
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_driver = False

    def become_driver(self):
        self.is_driver = True
        print(f"{self.name} now a driver.")

    def drive(self, car):
        if self.is_driver:
            print(f"{self.name} drive a car {car.model}.")

class Car:
    def __init__(self, model):
        self.model = model
        self.is_running = False

    def start(self):
        self.is_running = True
        print(f"Car {self.model} on.")

    def stop(self):
        self.is_running = False
        print(f"Car {self.model} off.")

person1 = Human("nick", 25)
person2 = Human("nike", 30)
car1 = Car("Toyota")
car2 = Car("Honda")

car1.start()
car1.stop()