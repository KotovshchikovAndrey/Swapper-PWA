import typing as tp
from abc import ABC, abstractmethod

from core.entities import IUser
from database.connections import get_connection
from database.connections.postgres import PostgreSQLConnection
from database.models import Token, User
from database.repositories.base import SQLRepository


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
    async def delete(self, user_id: int, token: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def find_by_user_id_and_value(self, user_id: int, value: str) -> IUser:
        raise NotImplementedError()


class TokenPostgresRepository(SQLRepository, ITokenRepository):
    def __init__(self):
        super().__init__()

    async def create(self, user_instance: IUser, value: str):
        await self._model.objects.create(user=user_instance, value=value)

    async def update(self, user_instance: IUser, old_value: str, new_value: str):
        token = await self._model.objects.get(user=user_instance, value=old_value)
        token.value = new_value
        await token.update()

    async def delete(self, user_id: int, token: str):
        await self._model.objects.delete(user__id=user_id, value=token)

    async def find_by_user_id_and_value(self, user_id: int, value: str):
        return await self._model.objects.get_or_none(user__id=user_id, value=value)
