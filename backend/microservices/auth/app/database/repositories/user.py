import typing as tp
from abc import ABC, abstractmethod

from core.entities import IUser
from database.connections import get_connection
from database.connections.postgres import PostgreSQLConnection
from database.models import User
from database.repositories.base import SQLRepository


class IUserRepository(ABC):
    @abstractmethod
    async def find_by_id(self, id: int) -> tp.Optional[IUser]:
        raise NotImplementedError()

    @abstractmethod
    async def find_by_email(self, email: str) -> tp.Optional[IUser]:
        raise NotImplementedError()

    @abstractmethod
    async def create(
        self, name: str, email: str, password: str, phone: tp.Optional[str] = None
    ) -> IUser:
        raise NotImplementedError()


class UserPostgresRepository(SQLRepository, IUserRepository):
    def __init__(self):
        super().__init__()

    async def find_by_id(self, id: int):
        return await User.objects.get_or_none(id=id)

    async def find_by_email(self, email: str):
        return await self._model.objects.get_or_none(email=email)

    async def create(
        self, name: str, email: str, password: str, phone: tp.Optional[str] = None
    ):
        new_user = await self._model.objects.create(
            name=name,
            email=email,
            phone=phone,
            password=password,
        )

        return new_user
