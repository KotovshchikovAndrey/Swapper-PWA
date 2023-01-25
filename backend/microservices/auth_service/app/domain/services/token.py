import datetime
import typing as tp

import jwt

from config import AppConfig
from database.entities import UserEntity
from database.repositories import TokenRepository

__all__ = ("TokenService",)


class TokenService:
    __repository: TokenRepository

    def __init__(self, repository: TokenRepository) -> None:
        self.__repository = repository

    async def create_token_pair(
        self, user: UserEntity, payload: dict
    ) -> tp.Tuple[str, str]:
        access_token = self.__generate_access_token(payload)
        access_token_part = self.__get_access_token_part(access_token)
        refresh_token = self.__generate_refresh_token(payload, access_token_part)
        await self.__repository.create(user, value=refresh_token)

        return access_token, refresh_token

    async def update_token_pair(
        self,
        user: UserEntity,
        old_refresh_token: str,
        payload: dict,
    ) -> tp.Tuple[str, str]:
        new_access_token = self.__generate_access_token(payload)
        access_token_part = self.__get_access_token_part(new_access_token)
        new_refresh_token = self.__generate_refresh_token(payload, access_token_part)

        await self.__repository.update(
            user_instance=user,
            old_value=old_refresh_token,
            new_value=new_refresh_token,
        )

        return new_access_token, new_refresh_token

    async def check_token_in_db(self, user_id: id, token: str) -> bool:
        token_in_db = await self.__repository.find_by_user_id_and_value(
            user_id, value=token
        )
        if token_in_db is not None:
            return True

        return False

    def decode_access_token(self, token: str) -> tp.Optional[dict]:
        try:
            payload = jwt.decode(
                jwt=token,
                key=AppConfig.get_secret_key(),
                algorithms=["HS256"],
            )

            return payload
        except jwt.InvalidTokenError:
            return None

    def decode_refresh_token(
        self, refresh_token: str, access_token: str
    ) -> tp.Optional[dict]:
        access_token_part = self.__get_access_token_part(access_token)
        try:
            payload = jwt.decode(
                jwt=refresh_token,
                key=AppConfig.get_secret_key() + access_token_part,
                algorithms=["HS256"],
            )

            return payload
        except jwt.InvalidTokenError:
            return None

    async def remove_token_from_db(self, user_id: int, token: str) -> None:
        await self.__repository.delete(user_id, token)

    def __generate_access_token(self, payload: dict):
        access_payload = {
            **payload,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc)
            + datetime.timedelta(minutes=30),
        }

        token = jwt.encode(
            payload=access_payload,
            key=AppConfig.get_secret_key(),
            algorithm="HS256",
        )

        return token

    def __generate_refresh_token(self, payload: dict, access_token_part: str):
        refresh_payload = {
            **payload,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc)
            + datetime.timedelta(days=30),
        }

        token = jwt.encode(
            payload=refresh_payload,
            key=AppConfig.get_secret_key() + access_token_part,
            algorithm="HS256",
        )

        return token

    def __get_access_token_part(self, access_token: str):
        token_length = len(access_token)
        start_slice = token_length // 3
        end_slice = token_length // 2

        return access_token[start_slice:end_slice]
