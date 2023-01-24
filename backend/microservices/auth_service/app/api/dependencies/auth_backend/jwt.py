import typing as tp

from fastapi.requests import Request
from domain.services import TokenService
from errors.api import ApiError


class JwtAuthBackend:
    __service: TokenService
    __check_refresh_token: bool

    def __init__(
        self, service: TokenService, check_refresh_token: bool = False
    ) -> None:
        self.__service = service
        self.__check_refresh_token = check_refresh_token

    def __call__(self, request: Request) -> None:
        access_token = request.headers.get("authorization", None)
        if access_token is None:
            raise ApiError.unauthorized(message="Токен авторизации не был передан!")

        payload = self.__service.decode_access_token(token=access_token)
        if payload is None:
            raise ApiError.forbidden(message="Невалидный токен!")

        if self.__check_refresh_token:
            refresh_token = request.cookies.get("refresh_token", None)
            if refresh_token is None:
                raise ApiError.forbidden(message="Токен обновления не был передан!")

            payload = self.__service.decode_refresh_token(refresh_token, access_token)
            if payload is None:
                raise ApiError.forbidden(message="Невалидный токен!")

        setattr(request, "user_payload", payload)
