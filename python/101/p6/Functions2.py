 # Create a function with three parameters
def product_price(price, quantity=1, discount=0):
    # Calculate the total price
    total = price * quantity

    # Apply the discount
    total = total - (total * discount / 100)

    return total


# Price only
print(product_price(100))

# Price and quantity
print(product_price(100, 3))

# Price and discount
print(product_price(100, discount=10))

# Price and quantity and discount
print(product_price(100, 3, 10))
