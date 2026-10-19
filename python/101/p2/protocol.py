 
# Creates an integer, string, list, and dictionary.
number = 10
text = "Python"
numbers = [1, 2, 3]
person = {"name": "Ali", "age": 25}


# Use the + Operator
print(number + 5)
print(text + " Programming")
print(numbers + [4, 5])


# Use the * Operator
print(number * 3)
print(text * 3)
print(numbers * 2)


# Use len()
print(len(text))
print(len(numbers))
print(len(person))

# Use the in Operator
print("Py" in text)
print(2 in numbers)
print("name" in person)


# Use for Loop
for letter in text:
    print(letter)

for n in numbers:
    print(n)

for key in person:
    print(key)
