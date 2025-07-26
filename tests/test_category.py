def test_category(category_sample_1, category_sample_2):
    assert category_sample_1.name == "Телевизоры"
    assert category_sample_1.description == ("Современный телевизор, который позволяет наслаждаться просмотром,"
                                             " станет вашим другом и помощником")
    product_4 = category_sample_1.products[0]
    assert product_4.name == '55" QLED 4K'
    assert product_4.description == "Фоновая подсветка"
    assert product_4.price == 123000.0
    assert product_4.quantity == 7

    assert category_sample_2.name == "Смартфоны"
    assert category_sample_2.description == ("Смартфоны, как средство не только коммуникации,"
                                             " но и получения дополнительных функций для удобства жизни")
    product_1 = category_sample_2.products[0]
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5

    assert category_sample_1.category_count == 2
    assert category_sample_1.product_count == 2
