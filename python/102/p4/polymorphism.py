# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Animal makes a sound")

    def info(self):
        print(self.name)


# Child class Dog
class Dog(Animal):
    def make_sound(self):
        print("Woof")


# Child class Cat
class Cat(Animal):
    def make_sound(self):
        print("Meow")


# Create objects
dog = Dog("Dog 1")
cat = Cat("Cat 1")

# Store objects in a list
animals = [dog, cat]

# Loop through objects
for animal in animals:
    animal.info()
    animal.make_sound()
