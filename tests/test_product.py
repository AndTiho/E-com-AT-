

def test_product(product_sample_1):
    assert product_sample_1.name == "55\" QLED 4K"
    assert product_sample_1.description == "Фоновая подсветка"
    assert product_sample_1.price == 123000.0
    assert product_sample_1.quantity == 7