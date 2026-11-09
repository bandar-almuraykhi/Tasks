from library import Library
from book_exceptions import BookNotFoundError, BorrowLimitError


library = Library(1, "My Library", 3)

library.load_books()




def view_books():

    print("===== ALL AVAILABLE BOOKS =====")

    if not library.books:
        print("No available books.")

    else:
        for book in library.books:
            print(book.get_details())

            
#view_books()

def view_borrowed_books():

    print("===== BORROWED BOOKS =====")

    if not library.borrowed_books:
        print("No books borrowed.")

    else:
        for book in library.borrowed_books:
            print(book.get_details())


#view_borrowed_books()

def borrow_book():

    try:
        book_id = int(input("Enter Book ID: "))

        library.borrow_book(book_id)

    except (BookNotFoundError, BorrowLimitError) as e:
        print(e)

    except ValueError:
        print("Please enter a valid book ID.")


def return_book():

    try:
        book_id = int(input("Enter Book ID: "))

        library.return_book(book_id)

    except BookNotFoundError as e:
        print(e)

    except ValueError:
        print("Please enter a valid book ID.")




while True:

    print("===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. View All Available Books")
    print("2. View Borrowed Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_books()

    elif choice == "2":
        view_borrowed_books()

    elif choice == "3":
        borrow_book()

    elif choice == "4":
        return_book()

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose from 0 to 4.")
