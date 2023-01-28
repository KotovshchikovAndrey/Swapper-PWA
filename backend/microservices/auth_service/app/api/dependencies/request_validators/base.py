import typing as tp
from abc import ABC

from fastapi.requests import Request

from errors.api import ApiError

__all__ = ("RequestValidator",)


class RequestValidator(ABC):
    _fields: tp.Tuple[str]
    _valid_data: tp.Dict[str, tp.Any]
    _errors: tp.List[str]

    def __init__(self, fields: tp.Tuple[str]) -> None:
        self._fields = fields
        self._valid_data = {}
        self._errors = []

    async def validate(self, request: Request) -> tp.Union[None, ApiError]:
        data: tp.Dict[str, tp.Any] = await request.json()

        # Поочередный вызов методов для валидации каждого поля из DTO
        for field in self._fields:
            try:
                getattr(self, f"validate_{field}")(data.get(field))
            except AttributeError:
                print(f"Не реализован метод валидации для поля {field}")
            else:
                self._valid_data[field] = data.get(field)

        if self._errors:
            raise ApiError.bad_request(
                message="Переданы невалидные данные", details=self._errors
            )

    def validate_id(self, id_param: str) -> None:
        if id_param is None:
            self._errors.append("параметр id не был передан")
            return

        if not id_param.isdigit():
            self._errors.append("параметр id должен быть числом")
