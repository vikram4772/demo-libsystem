class Library:
    # Represents a library that manages a collection of books and user borrowing records using tuples.
    def __init__(self, name):
        self.name = name
        self.books = []  # List of books represented as tuples (title, author, is_available, borrowed_by)
        self.user_records = {}  # Keeps track of books borrowed by each user

    def add_book(self, title, author):
        # Adds a new book to the library if it doesn't already exist.
        if any(book[0].lower() == title.lower() for book in self.books):
            print(f"The book '{title}' already exists in {self.name}.")
            return
        self.books.append((title, author, True, None))  # Book is added as a tuple
        print(f"The book '{title}' by {author} has been added to {self.name}.")

    def view_books(self):
        # Displays all books in the library along with their availability status.
        print("Books in the library:")
        for book in self.books:
            status = "Available" if book[2] else f"Borrowed by {book[3]}"
            print(f"- {book[0]} by {book[1]} ({status})")

    def search_book(self, title):
        # Searches for a book by title and displays its details if found.
        for book in self.books:
            if book[0].lower() == title.lower():
                status = "Available" if book[2] else f"Borrowed by {book[3]}"
                print(f"Book found: {book[0]} by {book[1]} ({status})")
                return
        print(f"The book '{title}' is not found in the library.")

    def borrow_book(self, user, title):
        # Allows a user to borrow a book if it is available and the user has not exceeded the borrowing limit.
        if user.name not in self.user_records:
            self.user_records[user.name] = []

        if len(self.user_records[user.name]) >= 3:
            print(f"{user.name} cannot borrow more than 3 books.")
            return

        for i, book in enumerate(self.books):
            if book[0].lower() == title.lower():
                if book[2]:  # Check availability
                    # Update the book tuple to mark it as borrowed
                    self.books[i] = (book[0], book[1], False, user.name)
                    self.user_records[user.name].append(book[0])
                    user.borrow_book(book[0])
                    print(f"The book '{title}' has been issued to {user.name}.")
                    return
                else:
                    print(f"The book '{title}' is currently not available.")
                    return
        print(f"The book '{title}' is not found in the library.")

    def return_book(self, user, title):
        # Allows a user to return a borrowed book.
        for i, book in enumerate(self.books):
            if book[0].lower() == title.lower() and book[3] == user.name:
                # Update the book tuple to mark it as returned
                self.books[i] = (book[0], book[1], True, None)
                self.user_records[user.name].remove(book[0])
                user.return_book(book[0])
                print(f"The book '{title}' has been returned by {user.name}.")
                return
        print(f"The book '{title}' is not associated with {user.name}.")


class User:
    # Represents a library user with attributes such as name, age, class, and the list of borrowed books.
    def __init__(self, name, age, clas):
        self.name = name
        self.age = age
        self.clas = clas
        self.borrowed_books = []  # List of borrowed book titles

    def borrow_book(self, title):
        # Adds a book title to the user's list of borrowed books.
        self.borrowed_books.append(title)

    def return_book(self, title):        
        self.borrowed_books.remove(title)

    def view_borrowed_books(self):
        # Displays the list of books borrowed by the user.
        print(f"Books borrowed by {self.name}:")
        for title in self.borrowed_books:
            print(f"- {title}")


# # Example Usage
# library = Library("Central Library")
# user1 = User("Harry", 19, 10)
# user2 = User("Bob", 20, 11)

# library.add_book("Harry Potter", "J.K. Rowling")
# library.add_book("The Hobbit", "J.R.R. Tolkien")
# library.add_book("1984", "George Orwell")
# library.add_book("1985", "George Orwell")

# library.view_books()
# library.borrow_book(user1, "Harry Potter")
# library.borrow_book(user1, "The Hobbit")
# library.borrow_book(user1, "1984")  # Should fail as user can only borrow 3 books
# library.borrow_book(user1, "1985")

# user1.view_borrowed_books()
# library.return_book(user1, "Harry Potter")
# library.view_books()
# user1.view_borrowed_books()