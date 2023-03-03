import typing as tp
from abc import ABC, abstractmethod

from core.entities import IUser
from database.models import User
from database.repositories.base import SQLRepository

repository = None


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

    async def find_by_id(self, id: int):  # type: ignore
        return await User.objects.get_or_none(id=id)

    async def find_by_email(self, email: str):  # type: ignore
        return await User.objects.get_or_none(email=email)

    async def create(  # type: ignore
        self, name: str, email: str, password: str, phone: tp.Optional[str] = None
    ):
        new_user = await User.objects.create(
            name=name,
            email=email,
            phone=phone,
            password=password,
        )

        return new_user


# Current UserRepository implementation for import
def get_user_repository(use_cache: bool = True) -> IUserRepository:
    if (repository is not None) and use_cache:
        return repository

    return UserPostgresRepository()
