import importlib
from typing import Any, Dict

class DatasetFactory:
    """
    Factory for creating dataset iterators.
    Supports both built-in types and dynamic loading from custom packages.
    """
    
    _iterators = {}

    @classmethod
    def register(cls, name: str, iterator_cls: Any):
        cls._iterators[name] = iterator_cls

    @classmethod
    def create(cls, type_name: str, **kwargs) -> Any:
        """
        Creates a dataset iterator instance.
        
        Args:
            type_name: The type of iterator (e.g., 'huggingface', 'custom_pkg.MyIterator').
            **kwargs: Arguments for the iterator constructor.
            
        Returns:
            An instance of the iterator.
        """
        if "." in type_name and type_name not in cls._iterators:
            try:
                module_name, class_name = type_name.rsplit(".", 1)
                module = importlib.import_module(module_name)
                iterator_cls = getattr(module, class_name)
                return iterator_cls(**kwargs)
            except (ImportError, AttributeError) as e:
                raise ValueError(f"Could not dynamically load dataset iterator {type_name}: {e}")

        if type_name not in cls._iterators:
            raise ValueError(f"Dataset iterator type {type_name} not registered")
            
        return cls._iterators[type_name](**kwargs)