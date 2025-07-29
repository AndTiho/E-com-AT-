from src.utils import create_object_from_json, json_to_python_data


def test_json_to_python_data():
    data = json_to_python_data("../data/products.json")
    assert data[1] == {
        "name": "Телевизоры",
        "description": "Современный телевизор, который позволяет наслаждаться просмотром,"
                       " станет вашим другом и помощником",
        "products": [{"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}],
    }


def test_create_object_from_json(json_test_data):
    test_data = create_object_from_json(json_test_data)
    assert test_data[0].name == "Телевизоры"
