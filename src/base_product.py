from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):

    @abstractmethod
    def __add__(self, other) -> Any:
        pass # pragma: no cover

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs) -> Any:
        pass # pragma: no cover
