from models.user import User
import config
import logging

class UserManager:
    """Manages user operations: adding, listing, searching, updating, deleting."""

    def __init__(self, storage):
        """Initializes a UserManager object."""
        self.storage = storage
        self.users = self.load_users()

    def add_user(self, name, user_id): # Correct the arguments here
        """Adds a new user to the system."""
        
        # Basic input validation (you might want to enhance this)
        if not all([name, user_id]):
            print("Both name and user ID are required.")
            return

        if self.find_user_by_id(user_id):
            print("A user with this ID already exists.")
            return

        user = User(name, user_id)
        self.users.append(user)
        self.save_users()
        logging.info(f"User added: Name - {name}, User ID - {user_id}")
        print("User added successfully!")

    def list_users(self):
        """Lists all users in the system."""
        if not self.users:
            print("No users in the system yet.")
            return

        for user in self.users:
            print(user) 

    def update_user(self):
        """Updates user details."""
        user_id_to_update = input("Enter the ID of the user to update: ")
        user = self.find_user_by_id(user_id_to_update)

        if not user:
            print(f"User with ID '{user_id_to_update}' not found.")
            return

        print(f"Updating user: {user}")

        user.name = input(f"Enter new name (leave blank to keep '{user.name}'): ") or user.name
        self.save_users()
        logging.info(f"User updated: User ID - {user.user_id}, New Name - {user.name}") 
        print("User updated successfully!")

    def delete_user(self):
        """Deletes a user from the system."""
        user_id_to_delete = input("Enter the ID of the user to delete: ")
        user_index = self.find_user_index_by_id(user_id_to_delete)

        if user_index is not None:
            del self.users[user_index]
            self.save_users()
            logging.info(f"User deleted: User ID - {user_id_to_delete}")
            print(f"User with ID '{user_id_to_delete}' deleted successfully.")
        else:
            print(f"User with ID '{user_id_to_delete}' not found.")

    def find_user_by_id(self, user_id):
        """Finds a user by their ID."""
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None 

    def find_user_index_by_id(self, user_id):
        """Finds the index of a user by their ID.
        Returns the index if found, otherwise None."""
        for index, user in enumerate(self.users):
            if user.user_id == user_id:
                return index
        return None

    def save_users(self):
        """Saves user data to the storage."""
        data = [vars(user) for user in self.users]
        self.storage.save(data, config.USERS_FILE) #Access using config

    def load_users(self):
        """Loads user data from the storage."""
        data = self.storage.load(config.USERS_FILE) #Access using config
        return [User(**user_data) for user_data in data]