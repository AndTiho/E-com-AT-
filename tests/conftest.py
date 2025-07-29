import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_sample_1():
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def product_sample_2():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def category_sample_1(product_sample_1):
    product4 = product_sample_1
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )


@pytest.fixture()
def category_sample_2(product_sample_2):
    product1 = product_sample_2
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций"
        " для удобства жизни",
        [product1],
    )


@pytest.fixture
def json_test_data():
    return [
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром,"
                           " станет вашим другом и помощником",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        }
    ]
