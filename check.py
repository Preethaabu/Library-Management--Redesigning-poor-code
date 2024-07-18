from models.book import Book
import config
import logging

class CheckoutManager:

    """Manages book checkout and check-in operations."""

    def __init__(self, book_manager, user_manager, storage):
        """Initializes a CheckoutManager object.

        Args:
            book_manager: An instance of the BookManager class.
            user_manager: An instance of the UserManager class.
            storage: An instance of the storage class.
        """
        self.book_manager = book_manager
        self.user_manager = user_manager
        self.storage = storage
        self.checkouts = self.load_checkouts()  

    def checkout_book(self, user_id, isbn):  # Include user_id and isbn as arguments
        """Checks out a book to a user."""
        user = self.user_manager.find_user_by_id(user_id)

        if not user:
            print("User not found!")
            return

        book = self.book_manager.find_book_by_isbn(isbn)

        if not book:
            print("Book not found!")
            return

        if not book.available:
            print("Book is already checked out.")
            return

        # Proceed with checkout
        book.available = False
        self.checkouts.append({"user_id": user_id, "isbn": isbn})
        self.save_checkouts()
        self.book_manager.save_books()  # Ensure the book's availability is updated
        logging.info(f"Book '{book.title}' checked out by user '{user.name}' (ISBN: {isbn})") 
        print(f"Book '{book.title}' checked out successfully to {user.name}.")

    def checkin_book(self, isbn):  # Add isbn as an argument 
        """Checks in a book."""
        checkout_to_remove = None
        for checkout in self.checkouts:
            if checkout["isbn"] == isbn:
                checkout_to_remove = checkout
                break

        if checkout_to_remove:
            self.checkouts.remove(checkout_to_remove)
            book = self.book_manager.find_book_by_isbn(isbn)
            if book:
                book.available = True 
                self.save_checkouts()
                self.book_manager.save_books()  # Ensure book availability is updated
                logging.info(f"Book '{book.title}' checked in (ISBN: {isbn})") 
                print(f"Book '{book.title}' checked in successfully.")
        else:
            print("This book is not currently checked out.")

    def list_checkouts(self):

        # Check if there are no checkouts
        if not self.checkouts:
            print("No books are checked out")
            return
        for checkout in self.checkouts:
            print(f"User ID: {checkout['user_id']}, ISBN: {checkout['isbn']}")

    def save_checkouts(self):
        """Saves checkout data to the storage."""
        self.storage.save(self.checkouts, config.CHECKOUTS_FILE)

    def load_checkouts(self):
        """Loads checkout data from the storage."""
        return self.storage.load(config.CHECKOUTS_FILE)