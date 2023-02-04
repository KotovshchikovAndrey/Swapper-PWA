import typing as tp

import jwt
from starlette.authentication import AuthCredentials, AuthenticationBackend, BaseUser
from starlette.requests import HTTPConnection

from core.config import AppConfig
from errors.exceptions.api import ApiError


class JwtUser(BaseUser):
    def __init__(self, id: int, email: str, token: str) -> None:
        self.id = id
        self.email = email
        self.token = token

    @property
    def is_authenticated(self) -> bool:
        return True

    def __str__(self) -> str:
        return self.email


class JwtAuthBackend(AuthenticationBackend):
    async def authenticate(self, conn: HTTPConnection):
        if "Authorization" not in conn.headers:
            return

        access_token = self.__get_access_token_from_request(conn)
        try:
            payload = self.__decode_access_token(access_token)
        except jwt.InvalidTokenError:
            raise ApiError.forbidden(message="Невалидный токен!")

        return (
            AuthCredentials(["authenticated"]),
            JwtUser(id=payload["id"], email=payload["email"], token=access_token),
        )

    def __decode_access_token(self, token: str) -> tp.Dict[str, tp.Any]:
        payload = jwt.decode(  # type: ignore
            jwt=token,
            key=AppConfig.get_secret_key(),
            algorithms=["HS256"],
        )

        return payload

    def __get_access_token_from_request(self, conn: HTTPConnection) -> str:
        access_token = conn.headers.get("authorization", None)
        if access_token is None:
            raise ApiError.unauthorized(message="Токен авторизации не был получен!")

        return access_token
