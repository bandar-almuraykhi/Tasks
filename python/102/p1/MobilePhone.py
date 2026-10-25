class MobilePhone:
    category = "Electronics"

    # Initialize phone details
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    # Display phone details
    def display_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)

    # Change category
    @classmethod
    def change_category(cls, new_category):
        cls.category = new_category


# Create two objects
phone1 = MobilePhone("Apple", "iPhone 16", 3500)
phone2 = MobilePhone("Samsung", "S25", 3000)

# Display phone details
phone1.display_details()
phone2.display_details()

# Change category
MobilePhone.change_category("Smart Devices")

# Display updated category
print(phone1.category)
print(phone2.category)
