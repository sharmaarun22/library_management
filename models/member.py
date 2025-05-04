from .person import Person
from .library import Library
from .book import Book

class Member(Person):
    def __init__(self, name, email, member_id, borrowed_books, library1:Library):
        super().__init__(name, email)
        self.member_id = member_id
        self.borrowed_books = borrowed_books
        self.library1 = library1

    def get_role(self):
        print("This is a member of library")

    def borrow_book(self, book_to_borrow:Book):
        if book_to_borrow in self.library1.books:
            if book_to_borrow.available:
                self.borrowed_books.append(book_to_borrow)
                book_to_borrow.available = False
        else:
            print("Book not available")

    def return_book(self, book_to_return):
        self.borrowed_books = list([book for book in self.borrowed_books if book != book_to_return])
        book_to_return.available = True

    def list_borrowed_books(self):
        borrowed_books = list([book.title for book in self.borrowed_books])
        print(f"Borrowed books are: {borrowed_books}")

    def __str__(self):
        return f"{self.name}, member_id: {self.member_id}"