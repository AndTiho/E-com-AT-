import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def json_to_python_data(path: str) -> Any:
    """Функция для преобразования JSON данных в данные для работы в Python"""
    full_path = os.path.join(os.path.dirname(__file__), path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_object_from_json(data: list) -> list:
    """Функция для обработки приходящих на вход данных в объект класса Продукт и Категория"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories
