# Dataset Factory

[English](README.md) | [Русский](README.ru.md)

Dynamic dataset iterator factory for VLMHyperBench. Supports both built-in and custom iterators via dot notation.

## Installation

```bash
pip install dataset_factory
```

## Usage

```python
from dataset_factory.factory import DatasetFactory

# Register internal
# DatasetFactory.register("local", LocalIterator)

# Dynamic load
iterator = DatasetFactory.create("my_custom_package.MyIterator", path="/data")