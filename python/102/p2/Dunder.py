class Vector2D:
    # Initialize x and y
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Add two vectors
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    # Display the vector
    def __str__(self):
        return f"({self.x}, {self.y})"


# Create two objects
v1 = Vector2D(2, 3)
v2 = Vector2D(4, 5)

# Add the vectors
result = v1 + v2

# Print the result
print(result)
