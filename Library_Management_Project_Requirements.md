
# 📘 Python OOP Project: Library Management System

## 🎯 Objective
Build a modular **Library Management System** to practice advanced OOP, file handling, inheritance, and real-world system design in Python.

---

## 🛠️ Requirements

### 1. Person (Abstract Class)
- Attributes: `name`, `email`
- Abstract method: `get_role()`

### 2. Member (Inherits from Person)
- Attributes:
  - `member_id`
  - `borrowed_books` (list of borrowed books)
- Methods:
  - `borrow_book(book)`
  - `return_book(book)`
  - `list_borrowed_books()`

### 3. Librarian (Inherits from Person)
- Permissions:
  - Add or remove books
  - Register new members
  - List all books and members

### 4. Book
- Attributes:
  - `title`
  - `author`
  - `isbn`
  - `available` (boolean indicating if the book can be borrowed)

### 5. Library
- Contains:
  - A collection of books
  - A list of members
- Methods:
  - `add_book(book)`
  - `remove_book(isbn)`
  - `find_book(title or isbn)`
  - `register_member(member)`
  - `get_summary()` – list of available books, borrowed books, and members

---

## ✅ OOP Concepts to Use

| Concept         | Where to Use                                 |
|----------------|-----------------------------------------------|
| Abstraction     | `Person` as abstract class                    |
| Inheritance     | `Member` and `Librarian` inherit from Person |
| Encapsulation   | Book availability state, borrowing logic     |
| Polymorphism    | `get_role()` behaves differently per role    |
| Composition     | `Library` contains `Book` and `Member` objects |
| File Handling   | (Optional) Save/load book and member data using JSON |

---

## 💡 Bonus Features (Optional)
- Save/load library data with JSON files
- Implement a command-line interface to interact with the system
- Add borrow limits, due dates, and fines for overdue books
- Track history of borrowed books

---

> Try to complete this project on your own to reinforce your object-oriented design thinking!
