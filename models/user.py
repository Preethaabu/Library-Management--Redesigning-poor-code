class User:
    """Represents a user in the library system."""

    def __init__(self, name, user_id):
        """Initializes a User object.

        Args:
            name (str): The name of the user.
            user_id (str): A unique identifier for the user.
        """
        self.name = name
        self.user_id = user_id

    def __str__(self):
        """Returns a string representation of the User object."""
        return f"Name: {self.name}, User ID: {self.user_id}" 