# Car Class
class Car:
    def __init__(self, id, brand, model, year, status="available"):
        self.id = id
        self.brand = brand
        self.model = model
        self.year = year
        self.status = status

    def calculate_daily_rate(self):
        return 0

    def is_available(self):
        return self.status == "available"

    def get_details(self):
        return (
            f"ID: {self.id}, Brand: {self.brand}, "
            f"Model: {self.model}, Year: {self.year}, "
            f"Status: {self.status}, "
            f"Daily Rate: {self.calculate_daily_rate()} SAR"
        )

    def __str__(self):
        return self.get_details()


# Economy Car Class
class EconomyCar(Car):
    def __init__(self, id, brand, model, year):
        super().__init__(id, brand, model, year)

    def calculate_daily_rate(self):
        return 100

    def get_details(self):
        return f"Type: Economy, {super().get_details()}"


# Luxury Car Class
class LuxuryCar(Car):
    def __init__(self, id, brand, model, year):
        super().__init__(id, brand, model, year)

    def calculate_daily_rate(self):
        return 350

    def get_details(self):
        return f"Type: Luxury, {super().get_details()}"


# Reservation Class
class Reservation:
    def __init__(self, id, customer_name, car, days):
        if days < 1:
            print("Days must be at least 1")

        self.id = id
        self.customer_name = customer_name
        self.car = car
        self.days = days
        self.status = "confirmed"

    def calculate_total_cost(self):
        return self.days * self.car.calculate_daily_rate() + 50

    def get_details(self):
        return (
            f"Reservation ID: {self.id}, "
            f"Customer: {self.customer_name}, "
            f"Car: {self.car.brand} {self.car.model}, "
            f"Days: {self.days}, "
            f"Status: {self.status}, "
            f"Total Cost: {self.calculate_total_cost()} SAR"
        )

    def __str__(self):
        return (
            f"Reservation ID: {self.id}, "
            f"Customer: {self.customer_name}, "
            f"Car: {self.car.brand} {self.car.model}, "
            f"Status: {self.status}"
        )


# Main Class
class Main:
    def __init__(self):

        # Cars List
        self.cars = [
            EconomyCar(1, "Toyota", "Yaris", 2023),
            EconomyCar(2, "Hyundai", "Accent", 2024),
            EconomyCar(3, "Kia", "Pegas", 2022),
            LuxuryCar(4, "Mercedes", "E-Class", 2024),
            LuxuryCar(5, "BMW", "5 Series", 2023)
        ]

        # Reservations List
        self.reservations = [
            Reservation(1, "Ahmed", self.cars[0], 3),
            Reservation(2, "Sara", self.cars[3], 2),
            Reservation(3, "Khalid", self.cars[1], 5)
        ]

        # Update reserved cars
        for reservation in self.reservations:
            reservation.car.status = "rented"

    # View Cars
    def view_cars(self):
        print("\n===== ALL CARS =====")

        for car in self.cars:
            print(car.get_details())

    # Create Reservation
    def create_reservation(self):
        customer_name = input("Customer name: ")
        car_id = int(input("Car ID: "))
        days = int(input("Number of rental days: "))
        reservation_id = int(input("Reservation ID: "))

        # Check Reservation ID
        for reservation in self.reservations:
            if reservation.id == reservation_id:
                print("Reservation ID already exists.")
                return

        # Find Car
        selected_car = None

        for car in self.cars:
            if car.id == car_id:
                selected_car = car
                break

        if selected_car is None:
            print("Car not found.")
            return

        # Check Availability
        if not selected_car.is_available():
            print("Car is not available.")
            return

        # Check Days
        if days < 1:
            print("Days must be at least 1")
            return

        # Create Reservation
        new_reservation = Reservation(
            reservation_id,
            customer_name,
            selected_car,
            days
        )

        self.reservations.append(new_reservation)

        # Update Car Status
        selected_car.status = "rented"

        print("Reservation created successfully.")
        print(new_reservation.get_details())

    # View Reservations
    def view_reservations(self):
        print("\n===== ALL RESERVATIONS =====")

        if not self.reservations:
            print("No reservations found.")
            return

        for reservation in self.reservations:
            print(reservation.get_details())

    # Menu
    def run(self):
        while True:
            print("\n===== CAR RENTAL SYSTEM =====")
            print("1. View All Cars")
            print("2. Create Reservation")
            print("3. View Reservations")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.view_cars()

            elif choice == "2":
                self.create_reservation()

            elif choice == "3":
                self.view_reservations()

            elif choice == "0":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please choose from 0 to 3.")


# Start Program
app = Main()
app.run()
