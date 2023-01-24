import typing as tp
from abc import ABC, abstractmethod

from database.entities import TokenEntity, UserEntity
from database.models import Token, User
from database.repositories.base import BaseSqlRepository


class TokenRepository(ABC):
    @abstractmethod
    async def create(self, user_instance: UserEntity, value: str) -> None:
        pass

    @abstractmethod
    async def update(self):
        pass

    @abstractmethod
    async def delete(self, user_id: int, token: str) -> None:
        pass


class TokenPostgreSQLRepository(BaseSqlRepository[tp.Type[Token]], TokenRepository):
    def __init__(self) -> None:
        super().__init__(model=Token)

    async def create(self, user_instance: User, value: str) -> None:
        await self._model.objects.create(user=user_instance, value=value)

    async def update(self):
        pass

    async def delete(self, user_id: int, token: str) -> None:
        await self._model.objects.delete(user__id=user_id, value=token)