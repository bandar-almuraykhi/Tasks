from abc import ABC, abstractmethod


class BorrowInterface(ABC):

    @abstractmethod
    def borrow(self, book_id):
        pass

    @abstractmethod
    def return_book(self):
        pass
