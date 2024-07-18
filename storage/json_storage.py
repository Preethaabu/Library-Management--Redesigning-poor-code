import json
import os
from .storage_interface import StorageInterface 

class JsonStorage(StorageInterface):
    """Provides JSON file storage for library data."""

    def save(self, data, file_path):
        """Saves the provided data to a JSON file.

        Args:
            data: The data to be saved (should be JSON serializable).
            file_path (str): The path to the JSON file for storage. 
        """

        try:
            # Ensure the directory for the file exists 
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)  # Save data with indentation for readability
        except (IOError, json.JSONDecodeError) as e:
            print(f"An error occurred while saving to {file_path}: {e}")

    def load(self, file_path):
        """Loads data from a JSON file.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            list or dict: The loaded data from the JSON file. Returns an empty list if the 
                         file is not found or an error occurs during loading.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            # This is expected if the file doesn't exist yet (first time running, etc.)
            # print(f"File not found: {file_path}")
            return [] 
        except (IOError, json.JSONDecodeError) as e:
            print(f"An error occurred while loading from {file_path}: {e}")
            return [] 