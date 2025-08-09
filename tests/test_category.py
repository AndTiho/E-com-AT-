import pytest

from src.category import Category
from src.exceptions import MyCustomError


def test_category(category_sample_1, category_sample_2):
    assert category_sample_1.name == "Телевизоры"
    assert category_sample_1.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром," " станет вашим другом и помощником"
    )
    product_4 = category_sample_1.get_products[0]
    assert product_4.name == '55" QLED 4K'
    assert product_4.description == "Фоновая подсветка"
    assert product_4.price == 123000.0
    assert product_4.quantity == 7

    assert category_sample_2.name == "Смартфоны"
    assert category_sample_2.description == (
        "Смартфоны, как средство не только коммуникации," " но и получения дополнительных функций для удобства жизни"
    )
    product_1 = category_sample_2.get_products[0]
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5

    assert category_sample_1.category_count == 2
    assert category_sample_1.product_count == 2

    assert category_sample_1.products == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'

    category_sample_1.add_product(product_1)

    assert category_sample_1.products == (
        '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n' "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
    )
    assert category_sample_1.product_count == 3


def test_category_str(category_sample_1):
    assert str(category_sample_1) == "Телевизоры, количество продуктов: 7 шт."


def test_errors(category_smart_1):
    with pytest.raises(MyCustomError):
        category_smart_1.add_product("Not a product")


def test_add_product(category_smart_1, smartphone_3):
    category_smart_1.add_product(smartphone_3)

    assert (
        category_smart_1.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )
    assert category_smart_1.category_count == 5

def test_products_0(category_empty):
    assert category_empty.middle_price() == 0

def test_middle_price(category_smart_1):
    assert category_smart_1.middle_price() == 195000.0
