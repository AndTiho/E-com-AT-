from unittest.mock import Mock, patch

from src.product import Product


def test_product(product_sample_1):
    assert product_sample_1.name == '55" QLED 4K'
    assert product_sample_1.description == "Фоновая подсветка"
    assert product_sample_1.price == 123000.0
    assert product_sample_1.quantity == 7

def test_new_product(new_product_dict, next_new_product_dict):
    test_prod_list = []
    new_product = Product.new_product(
        new_product_dict, test_prod_list)
    test_prod_list.append(new_product)

    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5

    same_new_product = Product.new_product(
        next_new_product_dict, test_prod_list)
    test_prod_list.append(same_new_product)

    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 200000.0
    assert new_product.quantity == 15

def test_price(capsys,product_sample_1):
    product_sample_1.price = -100
    assert product_sample_1.price == 123000.0
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"
    product_sample_1.price = 0
    assert product_sample_1.price == 123000.0


@patch('builtins.input', return_value='Y')
def test_price_with_input(mock_input):
    test_obj = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    test_obj.price = 80.0  # Установка текущей цены
    mock_input.assert_called_once()  # Проверяем вызов input
    assert test_obj.price == 80.0  # Проверяем изменение цены
