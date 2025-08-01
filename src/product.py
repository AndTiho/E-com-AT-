

class Product:
    """Класс определяющий содержание Продукта, таких как имя, описание, цена и количество"""

    name: str
    description: str
    price: float
    quantity: int


    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int


    ) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, prod_dict: dict, prod_list):
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
    def price(self):
        return self.__price


    @price.setter
    def price(self, value):
        if value <= 0.0:
            print('Цена не должна быть нулевая или отрицательная')
        elif self.__price > value:
            user_answer = input('Заявленная цена ниже текущей, заменить? Y/N')
            if user_answer.lower() == 'y':
                self.__price = value
