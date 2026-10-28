class Student:
    def __init__(self, name, age, id):
        self.name = name       # Public
        self._age = age        # Protected
        self.__id = id         # Private

    # Public method
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")
        print(f"ID: {self.__id}")

    # Private method
    def __change_name(self, new_name):
        self.name = new_name

    # Getter
    @property
    def id(self):
        return self.__id

    # Setter
    @id.setter
    def id(self, value):
        self.__id = value


# Create object
s = Student("Ali", 20, 101)

# Display student info
s.display_info()

# Change name using private method
s._Student__change_name("Ahmed")

# Update ID using setter
s.id = 202

# Display updated info
s.display_info()
