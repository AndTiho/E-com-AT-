import pytest


def test_smartphone(smartphone_1):
    assert smartphone_1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_1.price == 180000.0
    assert smartphone_1.quantity == 5
    assert smartphone_1.efficiency == 95.5
    assert smartphone_1.model == "S23 Ultra"
    assert smartphone_1.memory == 256
    assert smartphone_1.color == "Серый"


def test_sum(smartphone_1, smartphone_2):
    smartphone_sum = smartphone_1 + smartphone_2
    assert smartphone_sum == 2580000.0


def test_error(smartphone_1, grass_1):
    with pytest.raises(TypeError):
        print(smartphone_1 + grass_1)
