from .person import Person
from .library import Library
from .book import Book
from .member import Member

class Librarian(Person):

    def __init__(self, name, email, library: Library):
        super().__init__(name, email)
        self.library = library

    def get_role(self):
        print("This is Librarian")

    def add_book(self, book:Book, library:Library):
        """Add a new book to the library collection"""
        self.library.books.append(book)

    def remove_book(self, isbn):
        """Remove a book from the collection using its ISBN"""
        self.library.books = list(book for book in self.library.books if book.isbn != isbn)

    def find_book(self, identifier):
        """Find a book by title or ISBN"""
        for book in self.library.books:
            if identifier in (book.name, book.isbn):
                return book

    def list_books(self):
        """List all books in the library"""
        print(self.library.books)

    def register_member(self, member:Member):
        """Register a new member to the library"""
        self.library.members.append(member)

    def list_members(self):
        """List all registered members"""
        print(self.library.members)




