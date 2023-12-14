class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

def show_info(self):
    print(f"Name: {self.name}, Age: {self.age}")

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
         print("meow")

class Frog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print("ribbit")


