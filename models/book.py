class Book:
    """Represents a book in the library system."""

    def __init__(self, title, author, isbn, available=True):
        """Initializes a Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN (International Standard Book Number) of the book. 
        """

        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available # Books are initially available for checkout 

    def __str__(self):
        """Returns a string representation of the Book object."""
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.available}"