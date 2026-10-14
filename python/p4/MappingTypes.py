 # Create a dictionary
car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2025
}

# Print values
print(car["brand"])
print(car["model"])
print(car["year"])

# Add color
car["color"] = "Black"

# Remove brand 
car.pop("brand")

# Print final dictionary
print(car)
