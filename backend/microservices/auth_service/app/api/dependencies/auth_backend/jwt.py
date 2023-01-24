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

    def check_access_token(self, request: Request) -> dict:
        access_token = self.__get_access_token_from_request(request)
        payload = self.__service.decode_access_token(token=access_token)
        if payload is None:
            raise ApiError.forbidden(message="Невалидный токен!")

        return payload

    def check_refresh_token(self, request: Request) -> None:
        access_token = self.__get_access_token_from_request(request)
        refresh_token = request.cookies.get("refresh_token", None)
        if refresh_token is None:
            raise ApiError.forbidden(message="Токен обновления не был передан!")

        payload = self.__service.decode_refresh_token(refresh_token, access_token)
        if payload is None:
            raise ApiError.forbidden(message="Невалидный токен!")

    def __get_access_token_from_request(self, request: Request) -> str:
        access_token = request.headers.get("authorization", None)
        if access_token is None:
            raise ApiError.unauthorized(message="Токен авторизации не был передан!")

        return access_token
