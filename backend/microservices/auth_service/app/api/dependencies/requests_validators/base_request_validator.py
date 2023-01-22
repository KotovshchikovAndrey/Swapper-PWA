import typing as tp
from abc import ABC, abstractmethod

from fastapi.requests import Request

from errors.api_errors import ApiError

__all__ = ("RequestValidator",)


class RequestValidator(ABC):
    _errors: tp.List[str]

    def __init__(self, fields: tp.Tuple[str]) -> None:
        self._fields = fields
        self._errors = []

    @abstractmethod
    async def validate(self, request: Request):
        pass

    def validate_id(self, id_param: str) -> None:
        if id_param is None:
            self._errors.append("параметр id не был передан")
            return

        if not id_param.isdigit():
            self._errors.append("параметр id должен быть числом")
