import typing as tp
from abc import ABC, abstractmethod


class Validator(ABC):
    @abstractmethod
    def validate(self, value: tp.Any) -> bool:
        pass


class MaxLengthValidator(Validator):
    __max_length: int

    def __init__(self, max_length: int) -> None:
        self.__max_length = max_length

    def validate(self, value: str) -> bool:
        if len(value) > self.__max_length:
            return False

        return True


class RangeValidator(Validator):
    __num_range: tp.Tuple[int, int]

    def __init__(self, num_range: tp.Tuple[int, int]) -> None:
        self.__num_range = num_range

    def validate(self, value: int) -> bool:
        if not (self.__num_range[0] <= value <= self.__num_range[1]):
            return False

        return True
