import pytest
from dataset_factory.models import DatasetItem
from dataset_factory.interfaces import DatasetIterator
from dataset_factory.registry import DatasetRegistry
from dataset_factory.factory import DatasetFactory
from dataset_factory.base_iterator import BaseDatasetIterator

class CustomIterator(BaseDatasetIterator):
    def _load_items(self, **kwargs):
        self.items.append(DatasetItem(text="test item"))

def test_dataset_item_validation():
    item = DatasetItem(image_path="test.jpg", text="hello", metadata={"key": "value"})
    assert item.image_path == "test.jpg"
    assert item.text == "hello"
    assert item.metadata["key"] == "value"

def test_registry_and_factory():
    # Register
    DatasetRegistry.register("custom")(CustomIterator)
    
    # Get from registry
    cls = DatasetRegistry.get_iterator_class("custom")
    assert cls == CustomIterator
    
    # Create via factory
    iterator = DatasetFactory.create("custom", dataset_dir_path="/tmp")
    assert isinstance(iterator, CustomIterator)
    assert len(iterator) == 1
    assert iterator.get_item(0).text == "test item"

def test_factory_dynamic_loading():
    # Test dynamic loading using the class itself as a path (mocking module path)
    # In real scenario it would be "dataset_factory.examples.MockDatasetIterator"
    path = "dataset_factory.examples.MockDatasetIterator"
    iterator = DatasetFactory.create(path, dataset_dir_path="/tmp", count=3)
    assert len(iterator) == 3
    assert iterator.get_item(0).metadata["source"] == "mock"

def test_factory_not_found():
    with pytest.raises(ValueError, match="not found in registry"):
        DatasetFactory.create("non_existent", dataset_dir_path="/tmp")

def test_base_iterator_interface():
    iterator = CustomIterator(dataset_dir_path="/tmp")
    items = list(iterator)
    assert len(items) == 1
    assert isinstance(items[0], DatasetItem)