class Library:
    def __init__(self):
        self.members = []
        self.books = []

    def get_books(self):
        return self.books

    def get_members(self):
        return self.members

    def get_summary(self):
        """Print a summary of available books, borrowed books, and registered members"""
        print(f"Total number of books available are: {self.books}")
        print(f"Total number of registered members  are: {self.members}")
        borrowed_books = list([book for book in self.books if book.available == False])
        print(f"Total number of books borrowed are: {len(borrowed_books)}")