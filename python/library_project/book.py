from book_meta import BookMeta
from borrow_interface import BorrowInterface


class Book(metaclass=BookMeta):

    def __init__(self, id, title, author, year):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = "available"

    def get_details(self):
        return f"ID: {self.id}, Title: {self.title}, Author: {self.author}, Year: {self.year}"

    def is_available(self):
        return self.status == "available"



class PrintedBook(Book, BorrowInterface):

    def __init__(self, id, title, author, year):
        super().__init__(id, title, author, year)
        self.type = "Printed"
        self.status = "available"

    def get_details(self):
        return f"{super().get_details()}, Type: {self.type}"

    def borrow(self, book_id):
        self.status = "borrowed"
        return True

    def return_book(self):
        self.status = "available"
        return True


#book1 = PrintedBook(1, "Python Basics", "Ahmed", 2023)

#print(book1.get_details())
#print(book1.is_available())

#book1.borrow(1)
#print(book1.is_available())

#book1.return_book()
#print(book1.is_available())

class EBook(Book, BorrowInterface):

    def __init__(self, id, title, author, year):
        super().__init__(id, title, author, year)
        self.type = "EBook"
        self.status = "available"

    def get_details(self):
        return f"{super().get_details()}, Type: {self.type}"

    def borrow(self, book_id):
        self.status = "borrowed"
        return True

    def return_book(self):
        self.status = "available"
        return True

#book1 = EBook(4, "Data Science", "Mona", 2023)

#print(book1.get_details())
#print(book1.is_available())

#book1.borrow(4)
#print(book1.is_available())

#book1.return_book()
#print(book1.is_available())
