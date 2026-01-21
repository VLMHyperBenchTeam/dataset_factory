from typing import Any, Dict, Type, Callable
from .interfaces import DatasetIterator

class DatasetRegistry:
    """
    Registry for dataset iterators.
    """
    _iterators: Dict[str, Type[DatasetIterator]] = {}

    @classmethod
    def register(cls, name: str) -> Callable:
        """
        Decorator to register a dataset iterator class.
        """
        def wrapper(iterator_cls: Type[DatasetIterator]) -> Type[DatasetIterator]:
            cls._iterators[name] = iterator_cls
            return iterator_cls
        return wrapper

    @classmethod
    def get_iterator_class(cls, name: str) -> Type[DatasetIterator]:
        """
        Retrieves a registered iterator class by name.
        """
        if name not in cls._iterators:
            raise ValueError(f"Dataset iterator '{name}' is not registered.")
        return cls._iterators[name]

    @classmethod
    def list_registered(cls) -> Dict[str, Type[DatasetIterator]]:
        """
        Returns all registered iterators.
        """
        return cls._iterators.copy()