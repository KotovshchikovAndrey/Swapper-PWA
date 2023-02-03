import typing as tp
from abc import ABC, abstractmethod

from core.entities import TokenEntity, UserEntity


class UserRepository(ABC):
    @abstractmethod
    async def get_by_id(self, id: tp.Union[int, str]) -> tp.Optional[UserEntity]:
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


class TokenRepository(ABC):
    @abstractmethod
    async def create(self, user_instance: UserEntity, value: str) -> None:
        pass

    @abstractmethod
    async def update(
        self, user_instance: UserEntity, old_value: str, new_value: str
    ) -> None:
        pass

    @abstractmethod
    async def delete(self, user_id: int, token: str) -> None:
        pass

    @abstractmethod
    async def find_by_user_id_and_value(
        self, user_id: int, value: str
    ) -> tp.Optional[TokenEntity]:
        pass
