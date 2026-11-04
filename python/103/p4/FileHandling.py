# Create a file and write two lines
with open("example.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("This is the second line.\n")

# Open the file and read its content
with open("example.txt", "r") as file:
    print(file.read())
