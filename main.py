from models.book import Book
from models.library import Library
from models.member import Member
from models.librarian import Librarian

l1 = Library()
librarian1 = Librarian("Sagar Sharma", "sg.gmail.com", l1)
book1 = Book("Alchemist", "RK Gandhi", "book123", True)
book2 = Book("Half Girlfriend", "Chetan Bhagat", "book3421", True)
librarian1.add_book(book1, l1)
librarian1.add_book(book2, l1)
m1 = Member("Arun Sharma", "arun.sharma@gmail.com", "lib123", [], l1)
librarian1.register_member(m1)
m1.borrow_book(book1)
m1.list_borrowed_books()
l1.get_summary()
m1.return_book(book1)
l1.get_summary()