from abc import ABC, abstractmethod

class StorageInterface(ABC):
    """Defines the interface (contract) for data storage classes."""

    @abstractmethod
    def save(self, data, file_path):
        """Saves data to storage.

        Args:
            data: The data to be saved. The type and structure 
                  of data will depend on the storage implementation. 
            file_path: The path where the data should be saved.
        
        Raises:
            NotImplementedError: This is an abstract method and needs to be 
                                  implemented by concrete subclasses.
        """
        raise NotImplementedError

    @abstractmethod
    def load(self, file_path):
        """Loads data from storage.

        Args:
            file_path: The path from where the data should be loaded.

        Returns:
            The data loaded from storage. The return type and format will 
            depend on the storage implementation.

        Raises:
            NotImplementedError: This is an abstract method and needs to be 
                                  implemented by concrete subclasses. 
        """
        raise NotImplementedError