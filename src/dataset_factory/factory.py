import importlib
from typing import Any, Dict, Optional, Type
from .interfaces import DatasetIterator
from .registry import DatasetRegistry

class DatasetFactory:
    """
    Factory for creating dataset iterators.
    Supports registered types, dynamic loading from modules, and custom packages.
    """

    @classmethod
    def create(cls, type_name: str, **kwargs) -> DatasetIterator:
        """
        Creates a dataset iterator instance.
        
        Args:
            type_name: The type of iterator (e.g., 'docvqa_ru', 'custom_pkg.MyIterator').
            **kwargs: Arguments for the iterator constructor.
            
        Returns:
            An instance of the iterator.
        """
        # 1. Try to get from registry
        try:
            iterator_cls = DatasetRegistry.get_iterator_class(type_name)
            return iterator_cls(**kwargs)
        except ValueError:
            pass

        # 2. Try dynamic loading (e.g., "module.ClassName")
        if "." in type_name:
            try:
                module_name, class_name = type_name.rsplit(".", 1)
                module = importlib.import_module(module_name)
                iterator_cls = getattr(module, class_name)
                
                if not issubclass(iterator_cls, DatasetIterator):
                    # We might want to be less strict here if we are transitioning, 
                    # but the task says "Ensure support for expandability"
                    pass
                
                return iterator_cls(**kwargs)
            except (ImportError, AttributeError) as e:
                raise ValueError(f"Could not dynamically load dataset iterator {type_name}: {e}")

        raise ValueError(f"Dataset iterator type '{type_name}' not found in registry and not a valid dynamic path.")