from typing import Any


class Product:
    """Класс определяющий содержание Продукта, таких как имя, описание, цена и количество"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int


    ) -> None:
        """Инициируется объёкт включающий свойства'имя','описание','цена','кол-во'."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, prod_dict: dict, prod_list: list) -> Any:
        """ Метод создаёт объект класса Product из словаря.
        Если такой продукт уже существует, то добавляет к нему новое количество товара
        и если новая цена выше старой, то меняет её в большую сторону"""
        name = prod_dict['name']
        quantity = prod_dict['quantity']
        description = prod_dict['description']
        price = prod_dict['price']

        for prod in prod_list:
            if prod_dict['name'] == prod.name:
                prod.quantity += prod_dict['quantity']
                if prod_dict['price'] > prod.__price:
                    prod.__price = prod_dict['price']
            return prod
        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Геттер на получение приватного значения цены"""
        return self.__price

    @price.setter
    def price(self, value: int | float) -> None:
        """Сеттер принимает на вход новую цену товара и выполняет проверку на корректность.
        Если цена ниже имеющейся, то запрашивает у USER команду на замену цены"""
        if value <= 0.0:
            print('Цена не должна быть нулевая или отрицательная')
        elif self.__price > value:
            user_answer = input('Заявленная цена ниже текущей, заменить? Y/N')
            if user_answer.lower() == 'y':
                self.__price = value
        else:
            self.__price = value
