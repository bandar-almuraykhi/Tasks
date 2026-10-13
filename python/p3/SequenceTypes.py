 # Create Sequences

numbers_list = [10, 20, 30, 40, 50]
numbers_tuple = (10, 20, 30, 40, 50)
numbers_range = range(10, 60, 10)
text = "Python"


# Indexing

print(numbers_list[0])
print(numbers_tuple[1])
print(numbers_range[2])
print(text[3])


# Slicing

print(numbers_list[1:4])
print(numbers_tuple[0:3])
print(numbers_range[1:4])
print(text[1:4])


# Membership

print(30 in numbers_list)
print(60 not in numbers_tuple)
print(40 in numbers_range)
print("Py" in text)
