num_list = [45, 0, "abc"]

for value in num_list:
    try:
        print(100 / value)

    except TypeError:
        print("Invalid data type")

    except ZeroDivisionError:
        print("Cannot divide by zero")
