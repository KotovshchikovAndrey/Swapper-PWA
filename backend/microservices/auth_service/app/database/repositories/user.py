import typing as tp
from abc import ABC, abstractmethod

from database.entities import UserEntity
from database.models import User
from database.repositories.base import BaseSqlRepository


class UserRepository(ABC):
    @abstractmethod
    async def get_by_id(self, id: int) -> tp.Optional[UserEntity]:
        pass

    @abstractmethod
    async def create(
        self,
        name: str,
        surname: str,
        email: str,
        age: int,
        password: str,
        patronymic: tp.Optional[str] = None,
        phone: tp.Optional[str] = None,
    ) -> UserEntity:
        pass

    @abstractmethod
    async def find_by_email(self, email: str) -> tp.Optional[UserEntity]:
        pass

    @abstractmethod
    async def email_exists(self, email: str):
        pass


class UserPostgreSQLRepository(BaseSqlRepository[tp.Type[User]], UserRepository):
    def __init__(self) -> None:
        super().__init__(model=User)

    async def get_by_id(self, id: int) -> tp.Optional[User]:
        return await self._model.objects.get_or_none(id=id)

    async def create(
        self,
        name: str,
        surname: str,
        email: str,
        age: int,
        password: str,
        patronymic: tp.Optional[str] = None,
        phone: tp.Optional[str] = None,
    ) -> User:
        created_user = await self._model.objects.create(
            name=name,
            surname=surname,
            patronymic=patronymic,
            email=email,
            age=age,
            phone=phone,
            password=password,
        )

        return created_user

    async def find_by_email(self, email: str) -> tp.Optional[User]:
        return await self._model.objects.get_or_none(email=email)

    async def email_exists(self, email: str) -> bool:
        return await self._model.objects.filter(email=email).exists()
