# import typing as tp

from abc import ABC, abstractmethod

from core.entities import IUser
from database.models import Token
from database.repositories.base import SQLRepository

repository = None


class ITokenRepository(ABC):
    @abstractmethod
    async def create(self, user_instance: IUser, value: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def update(
        self, user_instance: IUser, old_value: str, new_value: str
    ) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, user: IUser, value: str) -> None:
        raise NotImplementedError()


class TokenPostgresRepository(SQLRepository, ITokenRepository):
    def __init__(self):
        super().__init__()

    async def create(self, user_instance: IUser, value: str):
        await Token.objects.create(user=user_instance, value=value)

    async def update(self, user_instance: IUser, old_value: str, new_value: str):
        token = await Token.objects.get(user=user_instance, value=old_value)
        token.value = new_value  # type: ignore
        await token.update()

    async def delete(self, user: IUser, value: str):
        await Token.objects.delete(user=user, value=value)


# Current TokenRepository implementation for import
def get_token_repository(use_cache: bool = True) -> ITokenRepository:
    if (repository is not None) and use_cache:
        return repository

    return TokenPostgresRepository()
