import unittest
from lib_managment_sys import Library, User

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library("Central Library")
        self.user = User("Harry", 19, 10)

        # Add books to the library
        self.library.add_book("Harry Potter", "J.K. Rowling")
        self.library.add_book("The Hobbit", "J.R.R. Tolkien")
        self.library.add_book("1984", "George Orwell")

    def test_add_existing_book(self):
        # Attempt to add an existing book should not duplicate it
        initial_count = len(self.library.books)
        self.library.add_book("Harry Potter", "J.K. Rowling")
        self.assertEqual(len(self.library.books), initial_count)  # No new book added

    def test_borrow_book(self):
        # User borrows a book
        self.library.borrow_book(self.user, "Harry Potter")
        # Book should now be unavailable
        for book in self.library.books:
            if book[0].lower() == "harry potter":
                self.assertFalse(book[2])
                self.assertEqual(book[3], "Harry")
        # User's borrowed books should reflect the borrowed book
        self.assertIn("Harry Potter", self.user.borrowed_books)

    def test_borrow_unavailable_book(self):
        # Borrow the same book twice - second time should fail to change anything
        self.library.borrow_book(self.user, "Harry Potter")
        # Try borrowing again
        self.library.borrow_book(self.user, "Harry Potter")
        # Check that user still only has 1 borrowed book
        self.assertEqual(len(self.user.borrowed_books), 1)
        # Check that book is still marked as borrowed by "Harry"
        for book in self.library.books:
            if book[0].lower() == "harry potter":
                self.assertFalse(book[2])
                self.assertEqual(book[3], "Harry")

    # def test_borrow_limit(self):
    #     # User borrows 3 books
    #     self.library.borrow_book(self.user, "Harry Potter")
    #     self.library.borrow_book(self.user, "The Hobbit")
    #     self.library.borrow_book(self.user, "1984")
    #     self.assertEqual(len(self.user.borrowed_books), 3)

    #     # Adding another book and trying to borrow should fail
    #     self.library.add_book("Brave New World", "Aldous Huxley")
    #     self.library.borrow_book(self.user, "Brave New World")
    #     # Still only 3 books borrowed by the user
    #     self.assertEqual(len(self.user.borrowed_books), 3)

    # def test_return_book(self):
    #     # Borrow a book
    #     self.library.borrow_book(self.user, "Harry Potter")
    #     # Return the book
    #     self.library.return_book(self.user, "Harry Potter")
    #     # Book should now be available again
    #     for book in self.library.books:
    #         if book[0].lower() == "harry potter":
    #             self.assertTrue(book[2])
    #             self.assertEqual(book[3], None)
    #     # User should not have the book anymore
    #     self.assertNotIn("Harry Potter", self.user.borrowed_books)

    # def test_return_non_borrowed_book(self):
    #     # Try returning a book the user never borrowed
    #     self.library.return_book(self.user, "The Hobbit")
    #     # Book remains available (was never borrowed)
    #     for book in self.library.books:
    #         if book[0].lower() == "the hobbit":
    #             self.assertTrue(book[2])
    #             self.assertEqual(book[3], None)
    #     # User should have no borrowed books
    #     self.assertEqual(len(self.user.borrowed_books), 0)


if __name__ == '__main__':
    unittest.main()
