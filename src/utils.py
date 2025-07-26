import json
import os

from src.category import Category
from src.product import Product


def json_to_python_data(path: str) -> dict:
    full_path = os.path.join(os.path.dirname(__file__), '../data/products.json')
    with open(full_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def create_object_from_json(data):
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category['products'] = products
        categories.append(Category(**category))

    return categories

#
#
# data = json_to_python_data('../data/products.json')
# print(data)
# # x, y = create_object_from_json(data)
# # print(x)
# # print(x.name)
# #
# # z = y.products
# # print(z.name)
