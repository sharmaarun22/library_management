from models.book import Book
from models.library import Library
from models.member import Member
from models.librarian import Librarian

l1 = Library()
librarian1 = Librarian("Sagar Sharma", "sg.gmail.com", l1)
book1 = Book("Alchemist", "RK Gandhi", "book123", True)
book2 = Book("Half Girlfriend", "Chetan Bhagat", "book3421", True)
m1 = Member("Arun Sharma", "arun.sharma@gmail.com", "lib123", None, l1)
librarian1.register_member(m1)
m1.borrow_book(book1)