from abc import ABC, abstractmethod

# Abstract Class
class Appliance(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    def turn_off(self):
        print("Appliance turned off!")


# Interface
class Chargeable(ABC):

    @abstractmethod
    def charge(self):
        pass


# Smartphone Class
class Smartphone(Appliance, Chargeable):

    def turn_on(self):
        print("Smartphone turned on!")

    def charge(self):
        print("Charging smartphone...")


# Create Object
phone = Smartphone()

phone.turn_on()
phone.charge()
phone.turn_off()
