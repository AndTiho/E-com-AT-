import pytest


def test_lawn_grass(grass_1):
    assert grass_1.name == "Газонная трава"
    assert grass_1.description == "Элитная трава для газона"
    assert grass_1.price == 500.0
    assert grass_1.quantity == 20
    assert grass_1.country == "Россия"
    assert grass_1.germination_period == "7 дней"
    assert grass_1.color == "Зеленый"


def test_sum(grass_1, grass_2):
    grass_sum = grass_1 + grass_2
    assert grass_sum == 16750.0


def test_error(grass_1, smartphone_1):
    with pytest.raises(TypeError):
        print(grass_1 + smartphone_1)
