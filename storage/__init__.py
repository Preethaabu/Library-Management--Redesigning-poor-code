from .storage_interface import StorageInterface
from .json_storage import JsonStorage

# Define what should be imported when someone uses "from storage import *"
__all__ = ["StorageInterface", "JsonStorage"] 