import typing as tp

from fastapi.requests import Request

from domain.services import TokenService
from errors.api import ApiError


class JwtAuthBackend:
    __service: TokenService

    def __init__(self, service: TokenService) -> None:
        self.__service = service

    def check_access_token(self, request: Request) -> tp.Dict[str, tp.Any]:
        access_token = self.__get_access_token_from_request(request)
        payload = self.__service.decode_access_token(token=access_token)

        return payload

    async def check_refresh_token(self, request: Request) -> tp.Dict[str, tp.Any]:
        refresh_token = request.cookies.get("refresh_token", None)
        if refresh_token is None:
            raise ApiError.forbidden(message="Токен обновления не был передан!")

        access_token = self.__get_access_token_from_request(request)
        payload = self.__service.decode_refresh_token(refresh_token, access_token)

        token_in_db = await self.__service.check_token_in_db(
            user_id=payload["id"],
            token=refresh_token,
        )
        if not token_in_db:
            raise ApiError.forbidden(message="Невалидный токен!")

        return payload

    def __get_access_token_from_request(self, request: Request) -> str:
        access_token = request.headers.get("authorization", None)
        if access_token is None:
            raise ApiError.unauthorized(message="Токен авторизации не был передан!")

        return access_token
