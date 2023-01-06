import typing as tp
from abc import ABC, abstractmethod

from database import models
from database.repositories.base import BaseSqlRepository


class UserRepository(ABC):
    @abstractmethod
    async def get_all(self):
        pass

    @abstractmethod
    async def get_by_id(self):
        pass

    @abstractmethod
    async def create(self, name: str, surname: str, patronymic: str, email: str):
        pass

    @abstractmethod
    async def update(self):
        pass

    @abstractmethod
    async def delete(self):
        pass


class UserPostgreSQLRepository(BaseSqlRepository[tp.Type[models.User]], UserRepository):
    def __init__(self) -> None:
        super().__init__(model=models.User)

    async def create(self, name: str, surname: str, patronymic: str, email: str):
        created_user = await self._model.objects.create(
            name=name, surname=surname, patronymic=patronymic, email=email
        )

        return created_user

    async def update(self):
        pass
