import typing as tp

import jwt
from starlette.authentication import AuthCredentials, AuthenticationBackend, BaseUser
from starlette.requests import HTTPConnection

from core import config
from core.entities import IUser
from database.repositories.user import get_user_repository
from errors.exceptions.api import ApiError


class JwtUser(BaseUser):
    def __init__(self, instance: IUser, token: str) -> None:
        self.instance = instance
        self.token = token

    @property
    def is_authenticated(self) -> bool:
        return True

    def __str__(self) -> str:
        return self.instance.email


class JwtAuthBackend(AuthenticationBackend):
    async def authenticate(self, conn: HTTPConnection):
        if "Authorization" not in conn.headers:
            return

        token = self.get_token_from_request(conn)
        try:
            payload = self.decode_token(token)
        except jwt.InvalidTokenError:
            raise ApiError.forbidden(message="Невалидный токен!")

        current_user = await get_user_repository().find_by_id(id=payload["id"])
        if current_user is None:
            raise ApiError.not_found(message="Пользователь не найден!")

        return (
            AuthCredentials(["authenticated"]),
            JwtUser(instance=current_user, token=token),
        )

    def decode_token(self, token: str) -> tp.Dict[str, tp.Any]:
        payload = jwt.decode(  # type: ignore
            jwt=token,
            key=config.SECTRET_KEY,  # type: ignore
            algorithms=["HS256"],
        )

        return payload

    def get_token_from_request(self, conn: HTTPConnection) -> str:
        token = conn.headers.get("authorization", None)
        if token is None:
            raise ApiError.unauthorized(message="Токен авторизации не был получен!")

        return token
