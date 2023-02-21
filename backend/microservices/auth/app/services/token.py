import datetime
import typing as tp

import jwt

from core import config
from utils.injector import injector

from core.entities import UserEntity
from core.interfaces.repositories import TokenRepository
from errors.exceptions.api import ApiError


class TokenService:
    repository: TokenRepository

    @injector.inject("TokenRepository")  # type: ignore
    def __init__(self, repository: TokenRepository) -> None:
        self.repository = repository

    async def create_token_pair(
        self, user: UserEntity, payload: tp.Dict[str, tp.Any]
    ) -> tp.Tuple[str, str]:
        access_token = self.generate_access_token(payload)
        access_token_part = self.get_access_token_part(access_token)
        refresh_token = self.generate_refresh_token(payload, access_token_part)
        await self.repository.create(user, value=refresh_token)

        return access_token, refresh_token

    async def update_token_pair(
        self, user: UserEntity, payload: tp.Dict[str, tp.Any], old_refresh_token: str
    ) -> tp.Tuple[str, str]:
        new_access_token = self.generate_access_token(payload)
        access_token_part = self.get_access_token_part(new_access_token)
        new_refresh_token = self.generate_refresh_token(payload, access_token_part)

        await self.repository.update(
            user_instance=user,
            old_value=old_refresh_token,
            new_value=new_refresh_token,
        )

        return new_access_token, new_refresh_token

    async def check_token_in_db(self, user_id: int, token: str) -> bool:
        token_in_db = await self.repository.find_by_user_id_and_value(
            user_id, value=token
        )
        if token_in_db is not None:
            return True

        return False

    def decode_refresh_token(
        self, refresh_token: str, access_token: str
    ) -> tp.Dict[str, tp.Any]:
        access_token_part = self.get_access_token_part(access_token)
        try:
            payload = jwt.decode(  # type: ignore
                jwt=refresh_token,
                key=config.SECTRET_KEY + access_token_part,  # type: ignore
                algorithms=["HS256"],
            )

            return payload
        except jwt.InvalidTokenError:
            raise ApiError.forbidden(message="Невалидный токен!")

    async def remove_token_from_db(self, user_id: int, token: str) -> None:
        await self.repository.delete(user_id, token)

    def generate_access_token(self, payload: tp.Dict[str, tp.Any]) -> str:
        access_payload = {
            **payload,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc)
            + datetime.timedelta(minutes=30),
        }

        token = jwt.encode(
            payload=access_payload,
            key=config.SECTRET_KEY,  # type: ignore
            algorithm="HS256",
        )

        return token

    def generate_refresh_token(
        self, payload: tp.Dict[str, tp.Any], access_token_part: str
    ) -> str:
        refresh_payload = {
            **payload,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc)
            + datetime.timedelta(days=30),
        }

        token = jwt.encode(
            payload=refresh_payload,
            key=config.SECTRET_KEY + access_token_part,  # type: ignore
            algorithm="HS256",
        )

        return token

    def get_access_token_part(self, access_token: str) -> str:
        signature = access_token.split(".")[-1]
        signature_length = len(signature)

        # индекс начала среза
        start_slice = signature_length // 3

        # индекс конца среза
        end_slice = signature_length // 2

        return signature[start_slice:end_slice]
