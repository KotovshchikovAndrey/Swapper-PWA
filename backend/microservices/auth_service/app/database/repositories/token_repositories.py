import typing as tp
from abc import ABC, abstractmethod

from database.models import Token, User
from database.repositories.base_repository import BaseSqlRepository


class TokenRepository(ABC):
    @abstractmethod
    async def create(self, user_instance, value: str):
        pass

    @abstractmethod
    async def update(self):
        pass

    @abstractmethod
    async def delete(self):
        pass


class TokenPostgreSQLRepository(BaseSqlRepository[tp.Type[Token]], TokenRepository):
    async def create(self, user_instance: User, value: str):
        pass

    async def update(self):
        pass

    async def delete(self):
        pass