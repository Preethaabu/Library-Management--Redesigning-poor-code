from models.book import Book
import config
import logging

class BookManager:
    """Manages book operations - adding, listing, searching, updating, deleting."""

    def __init__(self, storage):
        """Initializes a BookManager object.

        Args:
            storage: An instance of the storage class to handle data persistence.
        """
        self.storage = storage 
        self.books = self.load_books()

    def add_book(self, title, author, isbn):  # Add parameters here
        """Prompts the user for book details and adds the book to the system."""

        # Basic Input Validation 
        if not all([title, author, isbn]):
            print("All fields (title, author, ISBN) are required.")
            return

        if self.find_book_by_isbn(isbn):
            print("A book with this ISBN already exists.")
            return

        book = Book(title, author, isbn)
        self.books.append(book)
        self.save_books()
        logging.info(f"Book added: Title - {title}, Author - {author}, ISBN - {isbn}")
        print("Book added successfully!")

    def search_book(self, query): # Method in the `BookManager`
        """Searches for a book by title, author, or ISBN."""
        matches = []
        for book in self.books:
            if (query.lower() in book.title.lower() or
                query.lower() in book.author.lower() or
                query == book.isbn):
                matches.append(book)

        if matches:
            print("Search Results:")
            for book in matches:
                print(book)
        else:
            print(f"No books found matching '{query}'.")

    def list_books(self):
        """Lists all books in the library."""
        if not self.books:
            print("No books in the library yet.")
            return

        for book in self.books:
            print(book)  # Uses the __str__ method of the Book class

    def search_books(self):
        """Searches for books by title, author, or ISBN."""
        query = input("Enter your search query (title, author, or ISBN): ")
        matches = []
        for book in self.books:
            if (query.lower() in book.title.lower() or 
                query.lower() in book.author.lower() or
                query == book.isbn):
                matches.append(book)

        if matches:
            print("Search Results:")
            for book in matches:
                print(book)
        else:
            print(f"No books found matching '{query}'.")

    def update_book(self):
        """Updates book details by ISBN."""
        isbn_to_update = input("Enter ISBN of the book to update: ")
        book = self.find_book_by_isbn(isbn_to_update)

        if not book:
            print(f"Book with ISBN '{isbn_to_update}' not found.")
            return

        print(f"Updating book: {book}")  

        book.title = input(f"Enter new title (leave blank to keep '{book.title}'): ") or book.title
        book.author = input(f"Enter new author (leave blank to keep '{book.author}'): ") or book.author

        self.save_books()
        logging.info(
            f"Book updated: ISBN - {book.isbn}, New Title - {book.title}, "
            f"New Author - {book.author}"
        )
        print("Book updated successfully!")

    def delete_book(self):
        """Deletes a book from the system using its ISBN."""
        isbn_to_delete = input("Enter ISBN of the book to delete: ")
        book_index = self.find_book_index_by_isbn(isbn_to_delete)

        if book_index is not None:
            del self.books[book_index]
            self.save_books()
            logging.info(f"Book deleted: ISBN - {isbn_to_delete}")
            print(f"Book with ISBN '{isbn_to_delete}' deleted successfully.")
        else:
            print(f"Book with ISBN '{isbn_to_delete}' not found.")

    def check_book_availability(self): 
        """Checks and displays the availability of a book using its ISBN."""
        isbn_to_check = input("Enter ISBN of the book to check availability: ")
        book = self.find_book_by_isbn(isbn_to_check)

        if book:
            if book.available: 
                print(f"The book '{book.title}' is currently available.") 
            else:
                print(f"The book '{book.title}' is currently checked out.") 
        else:
            print(f"No book found with ISBN '{isbn_to_check}'.")
    
    def find_book_by_isbn(self, isbn):
        """Finds a book by its ISBN.

        Args:
            isbn (str): The ISBN of the book to find.

        Returns:
            Book: The book object if found, otherwise None. 
        """
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_book_index_by_isbn(self, isbn):
        """Finds the index of a book in the books list by its ISBN. 
        Returns the index of the book if found, or None if not. 
        """
        for index, book in enumerate(self.books):
            if book.isbn == isbn:
                return index
        return None

    def save_books(self):
        """Saves book data to the storage."""
        data = [vars(book) for book in self.books]
        self.storage.save(data, config.BOOKS_FILE) 

    def load_books(self):
        """Loads book data from the storage."""
        data = self.storage.load(config.BOOKS_FILE) #Updated
        return [Book(**book_data) for book_data in data] 