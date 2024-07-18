Library Management System
Overview
This Library Management System is designed to manage books, users, and book checkouts within a library setting. It provides functionalities to add, list, search, update, and delete books and users, as well as to manage book checkouts and returns.

Features
1. Manage Books
Add Book: Allows adding a new book to the library inventory.
List Books: Displays a list of all books currently in the library.
Search Book: Searches for a book by title, author, or ISBN.
Update Book: Updates details (title and author) of a book based on its ISBN.
Delete Book: Removes a book from the library inventory using its ISBN.
2. Manage Users
Add User: Registers a new user in the library system.
List Users: Displays a list of all registered users.
Update User: Updates the name of a user based on their user ID.
Delete User: Deletes a user from the system using their user ID.
3. Manage Checkouts
Checkout Book: Allows a user to borrow a book from the library by providing their user ID and the book's ISBN.
Return Book: Allows a user to return a borrowed book to the library using the book's ISBN.
List Checked Out Books: Displays a list of books currently checked out, showing the user ID and book's ISBN.
4. Data Persistence
All book, user, and checkout data is stored in separate JSON files (books.json, users.json, checkouts.json) located in the data directory.
Data is loaded from these files when the system starts and saved back to them after any changes.
How to Use
Setup:

Ensure Python is installed on your system.
Install required dependencies (json module).
Running the Application:

Open a terminal or command prompt.
Navigate to the directory containing main.py.
Run python main.py.
Menu Navigation:

Use the numeric keys (1-4) to navigate through different menu options.
Follow the prompts to perform actions such as adding books, registering users, checking out books, etc.
Error Handling:

The system provides basic error handling for incorrect inputs (e.g., non-numeric user IDs or ISBNs).
It ensures data integrity by validating inputs before processing them.
Logging:

Logs of operations are stored in library.log to track important system activities.
Dependencies
Python 3.x
json module (standard library)
