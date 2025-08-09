from abc import ABC, abstractmethod


class BaseOrderCategory(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass
