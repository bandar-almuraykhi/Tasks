from book import PrintedBook, EBook
from book_exceptions import BookNotFoundError, BorrowLimitError


class Library:

    def __init__(self, id, name, max_borrowed):
        self.id = id
        self.name = name
        self.max_borrowed = max_borrowed

        self.books = []
        self.borrowed_books = []

    def load_books(self):
        self.books.clear()
        self.borrowed_books.clear()

        # Read available books
        try:
            with open("library.txt", "r") as file:
                lines = file.readlines()

                for line in lines:
                    data = line.strip().split(",")

                    if len(data) != 5:
                        continue

                    id, title, author, year, book_type = data

                    if book_type == "Printed":
                        book = PrintedBook(int(id), title, author, int(year))
                        self.books.append(book)

                    elif book_type == "EBook":
                        book = EBook(int(id), title, author, int(year))
                        self.books.append(book)

        except FileNotFoundError:
            print("Error: library.txt file not found.")

        # Read borrowed books
        try:
            with open("borrowed.txt", "r") as file:
                lines = file.readlines()

                for line in lines:
                    data = line.strip().split(",")

                    if len(data) != 5:
                        continue

                    id, title, author, year, book_type = data

                    if book_type == "Printed":
                        book = PrintedBook(int(id), title, author, int(year))

                    elif book_type == "EBook":
                        book = EBook(int(id), title, author, int(year))

                    else:
                        continue

                    book.status = "borrowed"
                    self.borrowed_books.append(book)

        except FileNotFoundError:
            print("Error: borrowed.txt file not found.")

        print("Books loaded successfully.")



#library = Library(1, "My Library", 3)

#library.load_books()

#print(len(library.books))
#print(len(library.borrowed_books))


    def get_details(self):
       return f"Library ID: {self.id}, Name: {self.name}, Available Books: {len(self.books)}, Borrowed Books: {len(self.borrowed_books)}"



#library = Library(1, "My Library", 3)

#library.load_books()

#print(library.get_details())


    def save_books(self):

        # Save available books
        with open("library.txt", "w") as file:
            for book in self.books:
                file.write(
                    f"{book.id},{book.title},{book.author},{book.year},{book.type}\n"
                )

        # Save borrowed books
        with open("borrowed.txt", "w") as file:
            for book in self.borrowed_books:
                file.write(
                    f"{book.id},{book.title},{book.author},{book.year},{book.type}\n"
                )




    def borrow_book(self, book_id):

    # Search for available book
        for book in self.books:
            if book.id == book_id:
                break
        else:
        # Check if already borrowed
            for borrowed_book in self.borrowed_books:
                if borrowed_book.id == book_id:
                    raise BookNotFoundError("Book is already borrowed.")

            raise BookNotFoundError("Book not found.")

    # Check borrowing limit
        if len(self.borrowed_books) >= self.max_borrowed:
            raise BorrowLimitError("Borrowing limit reached.")

    # Borrow book
        book.borrow(book_id)

    # Move book between lists
        self.books.remove(book)
        self.borrowed_books.append(book)

    # Save changes
        self.save_books()

        print("Book borrowed successfully.")




    def return_book(self, book_id):

        # Search for borrowed book
        for book in self.borrowed_books:
            if book.id == book_id:
                break
        else:
            raise BookNotFoundError("Book not found in borrowed books.")

        # Return the book
        book.return_book()

        # Move book to available list
        self.borrowed_books.remove(book)
        self.books.append(book)

        # Save changes
        self.save_books()

        print("Book returned successfully.")
