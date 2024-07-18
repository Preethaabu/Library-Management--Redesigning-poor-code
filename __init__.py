"""
Library Management System - Package Initialization
"""

# Option 1: Import specific classes/functions for easy access
from .book import BookManager
from .user import UserManager
from .check import CheckoutManager
from .storage.json_storage import JsonStorage  

# Now you can import these directly from the package in other modules:
# from src import BookManager, UserManager, ...

# Option 2: Define an __all__ variable to specify what to import with *
__all__ = ["BookManager", "UserManager", "CheckoutManager", "JsonStorage"]
# from src import * will now import these specified classes/functions

# Option 3: Leave it empty (Python will still recognize src as a package)
#  from src.book import BookManager, etc.