# Dataset Factory

[English](README.md) | [Русский](README.ru.md)

Динамическая фабрика итераторов датасетов для VLMHyperBench. Поддерживает как встроенные, так и пользовательские итераторы через dot notation.

## Установка

```bash
pip install dataset_factory
```

## Использование

```python
from dataset_factory.factory import DatasetFactory

# Регистрация встроенных
# DatasetFactory.register("local", LocalIterator)

# Динамическая загрузка
iterator = DatasetFactory.create("my_custom_package.MyIterator", path="/data")