class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        """Mark the book as checked out"""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned/available"""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available"""
        return not self._is_checked_out

    def __str__(self):
        """String representation of the book"""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []  # Private list to store books

    def add_book(self, book):
        """Add a book to the library"""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise ValueError("Only Book objects can be added to the library")

    def check_out_book(self, title):
        """Check out a book by title"""
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"Successfully checked out: {title}")
                return
        print(f"Book '{title}' not found or already checked out")

    def return_book(self, title):
        """Return a book by title"""
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    print(f"Successfully returned: {title}")
                return
        print(f"Book '{title}' not found or already available")

    def list_available_books(self):
        """List all available books in the library"""
        available_books = [book for book in self._books if book.is_available()]

        if not available_books:
            print("No available books in the library")
        else:
            for book in available_books:
                print(book)