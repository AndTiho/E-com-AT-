import pytest

from src.exceptions import MyCustomError
from src.order import Order


def test_order(order_1):
    assert order_1.product.name == "Газонная трава"
    assert order_1.quantity == 5
    assert order_1.total == 2500


def test_quantity_is_gone(grass_1):
    with pytest.raises(TypeError) as excinfo:
        Order(grass_1, 105)
    assert str(excinfo.value) == "На складе осталось всего 20 шт. Газонная трава."


def test_str(order_1):
    assert str(order_1) == "Покупаете : Газонная трава в количеств: 5 шт. С вас 2500.0 руб."


def test_repr(order_1):
    assert repr(order_1) == "Order(Газонная трава, 5, 2500.0)"


def test_product_is_gone():
    with pytest.raises(MyCustomError) as excinfo:
        Order("", 105)
    assert str(excinfo.value) == "Переданный объект не является товаром"
