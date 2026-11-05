# Create a Metaclass
class VersionMeta(type):

    # Called when creating a class
    def __new__(mcls, name, bases, namespace):

        # Add VERSION automatically
        namespace["VERSION"] = 1.0

        # Create and return the class
        return super().__new__(mcls, name, bases, namespace)


# Create Car class using VersionMeta
class Car(metaclass=VersionMeta):
    pass


# Create Person class using VersionMeta
class Person(metaclass=VersionMeta):
    pass


# Print VERSION from both classes
print(Car.VERSION)
print(Person.VERSION)
