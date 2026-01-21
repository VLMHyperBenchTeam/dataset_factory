from abc import ABC, abstractmethod
from typing import Iterator, Optional
from .models import DatasetItem

class DatasetIterator(ABC):
    """
    Abstract base class for all dataset iterators.
    """

    @abstractmethod
    def __iter__(self) -> Iterator[DatasetItem]:
        """
        Returns an iterator over DatasetItem objects.
        """
        pass

    @abstractmethod
    def __len__(self) -> int:
        """
        Returns the total number of items in the dataset.
        """
        pass

    @abstractmethod
    def get_item(self, idx: int) -> DatasetItem:
        """
        Returns a specific item by its index.
        
        Args:
            idx: Index of the item.
            
        Returns:
            DatasetItem at the specified index.
        """
        pass