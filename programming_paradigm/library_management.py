# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title              # public attribute
        self.author = author            # public attribute
        self.__is_checked_out = False   # private attribute

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
        else:
            print(f"{self.title} is already checked out.")

    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
        else:
            print(f"{self.title} was not checked out.")

    def is_available(self):
        return not self.__is_checked_out


class Library:
    def __init__(self):
        self.__books = []  # private list to store Book objects

    def add_book(self, book):
        self.__books.append(book)

    def check_out_book(self, title):
        for book in self.__books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                else:
                    print(f"{title} is already checked out.")
                return
        print(f"{title} not found in library.")

    def return_book(self, title):
        for book in self.__books:
            if book.title == title:
                book.return_book()
                return
        print(f"{title} not found in library.")

    def list_available_books(self):
        available_books = [book for book in self.__books if book.is_available()]
        for book in available_books:
            print(f"{book.title} by {book.author}")
