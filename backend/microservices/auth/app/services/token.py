import datetime
import typing as tp

import jwt

from abc import ABC, abstractmethod

from core import config
from core.entities import IUser

from database.repositories.token import ITokenRepository, get_token_repository
from errors.exceptions.api import ApiError

service = None


class ITokenService(ABC):
    repository: ITokenRepository

    @abstractmethod
    async def set_token(self, user: IUser, token: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def update_token(self, user: IUser, token: str, new_token: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def remove_token(self, user: IUser, token: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def generate_access_token(self, payload: tp.Dict[str, tp.Any]) -> str:
        raise NotImplementedError()

    @abstractmethod
    def generate_refresh_token(
        self, access_token: str, payload: tp.Dict[str, tp.Any]
    ) -> str:
        raise NotImplementedError()

    @abstractmethod
    def decode_refresh_token(
        self, refresh_token: str, access_token: str
    ) -> tp.Dict[str, tp.Any]:
        raise NotImplementedError()


class TokenService(ITokenService):
    def __init__(self, repository: ITokenRepository = get_token_repository()):
        self.repository = repository

    async def set_token(self, user: IUser, token: str):
        await self.repository.create(user_instance=user, value=token)
        return None

    async def update_token(self, user: IUser, token: str, new_token: str):
        await self.repository.update(
            user_instance=user, old_value=token, new_value=new_token
        )

        return None

    async def remove_token(self, user: IUser, token: str):
        await self.repository.delete(user, value=token)
        return None

    def generate_access_token(self, payload: tp.Dict[str, tp.Any]) -> str:
        base_payload = {
            "exp": datetime.datetime.now(tz=datetime.timezone.utc)
            + datetime.timedelta(minutes=30),
        }

        payload.update(base_payload)

        token = jwt.encode(
            payload=payload,
            key=config.SECTRET_KEY,  # type: ignore
            algorithm="HS256",
        )

        return token

    def generate_refresh_token(self, access_token: str, payload: tp.Dict[str, tp.Any]):
        base_payload = {
            "exp": datetime.datetime.now(tz=datetime.timezone.utc)
            + datetime.timedelta(days=30),
        }

        payload.update(base_payload)

        access_token_part = self.get_access_token_part(access_token)
        token = jwt.encode(
            payload=payload,
            key=config.SECTRET_KEY + access_token_part,  # type: ignore
            algorithm="HS256",
        )

        return token

    def decode_refresh_token(self, refresh_token: str, access_token: str):
        access_token_part = self.get_access_token_part(access_token)
        try:
            payload = jwt.decode(
                jwt=refresh_token,
                key=config.SECTRET_KEY + access_token_part,
                algorithms=["HS256"],
            )
        except jwt.InvalidTokenError:
            raise ApiError.forbidden(message="Невалидный токен!")

        return payload

    def get_access_token_part(self, access_token: str) -> str:
        signature = access_token.split(".")[-1]
        signature_length = len(signature)

        # индекс начала среза
        start_slice = signature_length // 3

        # индекс конца среза
        end_slice = signature_length // 2

        return signature[start_slice:end_slice]


# Current TokenService implementation for import
def get_token_service(use_cache: bool = True) -> ITokenService:
    if (service is not None) and use_cache:
        return service

    return TokenService()
