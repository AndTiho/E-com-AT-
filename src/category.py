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
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def get_products(self) -> list:
        return self.__products

    @property
    def products(self) -> str:
        product_str = ''
        for product in self.__products:
            product_str += f'{product.name}, {product.price}. Остаток: {product.quantity}\n'
        return product_str

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1
