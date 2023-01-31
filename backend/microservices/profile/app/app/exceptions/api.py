from __future__ import annotations

import typing as tp


class ApiError:
    status_code: int
    message: str
    details: tp.List[str]

    def __init__(self, status_code: int, message: str, details: tp.List[str]) -> None:
        self.status_code = status_code
        self.message = message
        self.details = details

    @classmethod
    def bad_request(
        cls, message: str = "Некорректный запрос!", details: tp.List[str] = []
    ) -> ApiError:
        return cls(status_code=400, message=message, details=details)

    @classmethod
    def forbidden(
        cls, message: str = "Доступ запрещен!", details: tp.List[str] = []
    ) -> ApiError:
        return cls(status_code=403, message=message, details=details)

    def not_found(
        cls, message: str = "Объект не найден!", details: tp.List[str] = []
    ) -> ApiError:
        return cls(status_code=404, message=message, details=details)

    @classmethod
    def internal(
        cls, message: str = "Внутренняя ошибка сервера!", details: tp.List[str] = []
    ) -> ApiError:
        return cls(status_code=500, message=message, details=details)
