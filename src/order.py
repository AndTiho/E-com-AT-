from src.product import Product


class Order:
    """Класс-ссылка на то, какой товар был куплен, количество купленного товара, а также итоговая стоимость."""

    def __init__(self, product: Product, quantity: int) -> None:
        """Инициируем объект класса для оформления заказа включающий свойства:
        Товар, заказываемое количество, и общую стоимость заказываемого товара"""
        if not isinstance(product, Product):
            raise ValueError("Переданный объект не является товаром")

        self.product = product
        if product.quantity >= quantity:
            self.quantity = quantity
        else:
            raise TypeError(f"На складе осталось всего {product.quantity} шт. {product.name}.")

        self.total = self.total_price()

    def __str__(self) -> str:
        """Метод для вывода информации пользователю"""
        return f"Покупаете : {self.product.name} в количеств: {self.quantity} шт. С вас {self.total} руб."

    def __repr__(self) -> str:
        """Метод для вывода информации для отладки"""
        return f"{self.__class__.__name__}({self.product.name}, {self.quantity}, {self.total})"

    def total_price(self) -> float:
        """Метод для подсчёта финальной стоимости заказываемого товара"""
        return self.product.price * self.quantity
