from storage.json_storage import JsonStorage
from book import BookManager
from user import UserManager
from check import CheckoutManager
import logging
import config

def main_menu():
    """Displays the main menu and gets user choice."""
    print("\nLibrary Management System")
    print("1.  Manage Books")
    print("2.  Manage Users")
    print("3.  Check Book Availabiity")
    print("4.  Checkout/Check-in Books")
    print("5.  Exit")

    while True:
        try:
            choice = input("Enter choice (1-5): ")
            if choice in ['1', '2', '3', '4', '5']:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def manage_books(book_manager):
    """Provides options to manage books within the system."""
    while True:
        print("\nBook Management")
        print("1. Add Book")
        print("2. List Books")
        print("3. Search for a Book")
        print("4. Update Book") # You'll need to implement this in book.py
        print("5. Delete Book") # You'll need to implement this in book.py
        print("6. Back to Main Menu")

        try:
            choice = input("Enter choice (1-7): ")

            if choice == '1':
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                book_manager.add_book(title, author, isbn)
            elif choice == '2':
                book_manager.list_books()
            elif choice == '3':
                query = input("Enter your search query (title, author, or ISBN): ")
                book_manager.search_book(query) 
            elif choice == '4':
                book_manager.update_book() # Call the update function 
            elif choice == '5':
                book_manager.delete_book() # Call the delete function
            elif choice == '6':
                break                
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def manage_users(user_manager):
    """Provides options to manage users within the system."""
    while True:
        print("\nUser Management")
        print("1. Add User")
        print("2. List Users")
        print("3. Update User") # You'll need to implement this in user.py
        print("4. Delete User") # You'll need to implement this in user.py
        print("5. Back to Main Menu") 

        try:
            choice = input("Enter choice (1-5): ")

            if choice == '1':
                name = input("Enter user name: ")
                user_id = input("Enter user ID: ")
                user_manager.add_user(name, user_id)
            elif choice == '2':
                user_manager.list_users()
            elif choice == '3':
                user_manager.update_user() # Call the update function
            elif choice == '4':
                user_manager.delete_user() # Call the delete function
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.") 
        except ValueError:
            print("Invalid input. Please enter a number.")


def manage_checkouts(checkout_manager):
    """Provides options for book checkouts and check-ins."""
    while True:
        print("\nCheckout/Check-in Management")
        print("1. Checkout Book")
        print("2. Check-in Book")
        print("3. List Checkouts")
        print("4. Back to Main Menu")  

        try:
            choice = input("Enter choice (1-3): ")

            if choice == '1': 
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to checkout: ")
                checkout_manager.checkout_book(user_id, isbn)
            elif choice == '2':
                isbn = input("Enter the ISBN of the book to return: ")
                checkout_manager.checkin_book(isbn)
            elif choice == '3':
            # List all checkouts
                checkout_manager.list_checkouts()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.") 
        except ValueError:
            print("Invalid input. Please enter a number.") 

def main():
    """The main function of the application."""

    logging.basicConfig(
      filename= config.LOG_FILE,  # Set the log file name in config.py
      level=logging.INFO,  # Capture INFO level and above (DEBUG, WARNING, ERROR, CRITICAL)
      format='%(asctime)s - %(levelname)s - %(message)s'
    )

    storage = JsonStorage()
    book_manager = BookManager(storage)
    user_manager = UserManager(storage)
    checkout_manager = CheckoutManager(book_manager, user_manager, storage)

    while True:
        choice = main_menu()

        if choice == '1':
            manage_books(book_manager)
        elif choice == '2':
            manage_users(user_manager)
        elif choice == '3':
            book_manager.check_book_availability() 
        elif choice == '4':
            manage_checkouts(checkout_manager)
        elif choice == '5':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.") # Should theoretically never be reached 

if __name__ == "__main__":
    main()