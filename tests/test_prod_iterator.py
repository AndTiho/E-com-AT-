import pytest


def test_prod_iterator(prod_iterator):
    iter(prod_iterator)
    assert prod_iterator.index == 0
    assert next(prod_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(prod_iterator).description == "512GB, Gray space"
    assert next(prod_iterator).price == 31000.0

    with pytest.raises(StopIteration):
        next(prod_iterator)
