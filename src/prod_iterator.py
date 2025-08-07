from typing import Any

from src.category import Category


class ProductIterator:
    """Класс итератор для перебора продуктов в запрашиваемой категории"""

    def __init__(self, category_obj: Category) -> None:
        """Инициатор класса принимающий на вход категорию"""
        self.category = category_obj
        self.index = 0

    def __iter__(self) -> "ProductIterator":
        """Метод для начала точки отсчёта для итерации"""
        self.index = 0
        return self

    def __next__(self) -> Any:
        """Метод для итерации по продуктам в запрашиваемой категории.
        Когда продукты закончатся, вызывает исключение StopIteration"""
        if self.index < len(self.category.get_products):
            product = self.category.get_products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
