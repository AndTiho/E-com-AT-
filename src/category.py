from src.product import Product


class Category:
    """Класс определяющий Имя категории, её описание и список продуктов, которые входят в данную категорию.
    Так же имеет два атрибута класса для подсчёта количества категорий и продуктов"""

    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """Инициируется объёкт включающий свойства 'имя','описание','продукты'."""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        """Маги метод для вывода в строковой форме для пользователя наименование запрашиваемой категории
        и подсчёт сколько в данной категории всего товаров"""
        prod_count = 0
        for product in self.__products:
            prod_count += product.quantity
        return f"{self.name}, количество продуктов: {prod_count} шт."

    @property
    def get_products(self) -> list:
        """Свойство позволяющее получить данные из приватного атрибута продуктов"""
        return self.__products

    @property
    def products(self) -> str:
        """Свойство позволяющее получить данные из приватного атрибута продуктов
        в развёрнутом виде"""
        product_str = ""
        for product in self.__products:
            product_str += f"{product}\n"
        return product_str

    def add_product(self, product: Product | str) -> None:
        """Метод для добавления нового продукта в категорию, если:
        он является классом Продукты или его наследником"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError
