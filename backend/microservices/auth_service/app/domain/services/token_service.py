import datetime
import os
import typing as tp

import jwt

from config import AppConfig
from database.repositories import TokenRepository

__all__ = ("TokenService",)


class TokenService:
    def __init__(self, repository: TokenRepository) -> None:
        self.__repository = repository

    async def create_tokens_for_user(self, user, payload: dict) -> tp.Tuple[str, str]:
        access_token = self.__generate_access_token(payload)
        access_part = self.__get_access_part(access_token)
        refresh_token = self.__generate_refresh_token(payload, access_part=access_part)
        await self.__repository.create(user, value=refresh_token)

        return access_token, refresh_token

    def __generate_access_token(self, payload: dict):
        access_payload = {
            **payload,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc)
            + datetime.timedelta(minutes=30),
        }

        token = jwt.encode(
            payload=access_payload, key=AppConfig.get_secret_key(), algorithm="HS256"
        )

        return token

    def __generate_refresh_token(self, payload: dict, access_part: str):
        refresh_payload = {
            **payload,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc)
            + datetime.timedelta(days=30),
        }

        token = jwt.encode(
            payload=refresh_payload,
            key=AppConfig.get_secret_key() + access_part,
            algorithm="HS256",
        )

        return token

    def __get_access_part(self, access_token: str):
        token_length = len(access_token)
        start_slice = token_length // 3
        end_slice = token_length // 2

        return access_token[start_slice:end_slice]
