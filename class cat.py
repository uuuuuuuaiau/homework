class Cat:
    def __init__(self, name, age, health_status="Healthy"):
        self.name = name
        self.age = age
        self.health_status = health_status

    def feed(self):
        print(f"{self.name} is eating.")

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Health: {self.health_status}")

    def check_health(self):
        if self.health_status == "Healthy":
            print(f"{self.name} is healthy.")