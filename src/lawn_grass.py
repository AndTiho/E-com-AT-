from src.product import Product


class LawnGrass(Product):
    """Класс наследник Продукта, расширяет познания в Травах Газонных"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Инициируется объёкт Трава Газонная от родительского класса Продукты, добавляя такие свойства как:
        страна производитель, срок прорастания, цвет"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: "LawnGrass") -> float:
        """Маги метод для сложения двух продуктов в виде:
        (цена запрашиваемого товара * количество) + (цена другого товара * количество),
        если они оба являются классом Трава Газонная"""
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError
