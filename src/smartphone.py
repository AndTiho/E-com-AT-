from src.product import Product


class Smartphone(Product):
    """Класс наследник Продукта, расширяет познания в Смартфонах"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Инициируется объёкт Смартфон от родительского класса Продукты, добавляя такие свойства как:
        эффективность, модель, память и цвет"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: "Smartphone") -> float:
        """Маги метод для сложения двух продуктов в виде:
        (цена запрашиваемого товара * количество) + (цена другого товара * количество),
        если они оба являются классом Смартфоны"""
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError
