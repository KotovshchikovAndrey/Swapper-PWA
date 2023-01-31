import typing as tp

from rest_framework.request import Request
from rest_framework.response import Response
from app.exceptions.api import ApiError


class ErrorHandler:
    def __init__(self, get_response: tp.Callable):
        self.get_response = get_response

    def __call__(self, request: Request):
        try:
            return self.get_response(request)
        except Exception as exc:
            if isinstance(exc, ApiError):
                return Response(
                    status=exc.status_code,
                    data={"message": exc.message, "details": exc.details},
                )

            return Response(
                status=500,
                data={"message": "Непредвиденная ошибка сервера!", "details": []},
            )
