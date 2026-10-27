# Parent Class 
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Speed: {self.speed}")

    def start(self):
        print("Vehicle starting...")


# Child Class
class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def display_info(self):
        super().display_info()
        print(f"Fuel Type: {self.fuel_type}")


# Create Object
car = Car("Toyota", 120, "Petrol")

# Call Methods
car.display_info()
car.start()
