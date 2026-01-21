from .interfaces import DatasetIterator
from .models import DatasetItem
from .registry import DatasetRegistry
from .base_iterator import BaseDatasetIterator
from typing import Iterator, List

@DatasetRegistry.register("mock_iterator")
class MockDatasetIterator(BaseDatasetIterator):
    """
    A mock dataset iterator for testing purposes.
    """
    def _load_items(self, **kwargs):
        count = kwargs.get("count", 5)
        for i in range(count):
            self.items.append(DatasetItem(
                image_path=f"/path/to/image_{i}.jpg",
                text=f"Question {i}?",
                metadata={"id": i, "source": "mock"}
            ))