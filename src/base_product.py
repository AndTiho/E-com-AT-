from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):

    @abstractmethod
    def __add__(self, other) -> Any:
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs) -> Any:
        pass
