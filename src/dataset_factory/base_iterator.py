import os
from typing import Iterator, List, Any, Dict
from .interfaces import DatasetIterator
from .models import DatasetItem

class BaseDatasetIterator(DatasetIterator):
    """
    A base implementation of DatasetIterator that can be extended.
    """
    def __init__(self, dataset_dir_path: str, **kwargs):
        self.dataset_dir_path = dataset_dir_path
        self.items: List[DatasetItem] = []
        self._load_items(**kwargs)

    def _load_items(self, **kwargs):
        """
        To be implemented by subclasses to populate self.items.
        """
        pass

    def __iter__(self) -> Iterator[DatasetItem]:
        return iter(self.items)

    def __len__(self) -> int:
        return len(self.items)

    def get_item(self, idx: int) -> DatasetItem:
        return self.items[idx]