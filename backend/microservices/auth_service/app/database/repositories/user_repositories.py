import typing as tp
from abc import ABC, abstractmethod

from database.models import User
from database.repositories.base_repository import BaseSqlRepository


class UserRepository(ABC):
    # @abstractmethod
    # async def get_all(self):
    #     pass

    # @abstractmethod
    # async def get_by_id(self):
    #     pass

    @abstractmethod
    async def create(self, name: str, surname: str, patronymic: str, email: str):
        pass

    # @abstractmethod
    # async def update(self):
    #     pass

    # @abstractmethod
    # async def delete(self):
    #     pass

    @abstractmethod
    async def email_exists(self, email: str):
        pass


class UserPostgreSQLRepository(BaseSqlRepository[tp.Type[User]], UserRepository):
    def __init__(self) -> None:
        super().__init__(model=User)

    async def create(
        self, name: str, surname: str, patronymic: str, email: str
    ) -> User:
        created_user = await self._model.objects.create(
            name=name, surname=surname, patronymic=patronymic, email=email
        )

        return created_user

    async def email_exists(self, email: str) -> bool:
        return await self._model.objects.filter(email=email).exists()
