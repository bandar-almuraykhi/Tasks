 # Create a function with one parameter
def check_number(number):
    # Check if the number is even
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test the function
print(check_number(10))
print(check_number(7))
