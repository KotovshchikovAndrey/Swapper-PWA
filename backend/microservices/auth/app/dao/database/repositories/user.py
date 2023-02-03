import typing as tp

from databases import Database

from core.interfaces.repositories import UserRepository
from dao.database import postgres
from dao.database.models import User
from dao.database.repositories.base import BaseSqlRepository


class UserPostgreSQLRepository(BaseSqlRepository[User], UserRepository):
    __db_connection: Database

    def __init__(self) -> None:
        super().__init__(model=User)
        self.__db_connection = postgres.database

    async def get_by_id(self, id: tp.Union[int, str]) -> tp.Optional[User]:  # type: ignore
        return await super().get_by_id(id=id)

    async def create(  # type: ignore
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

    async def find_by_email(self, email: str) -> tp.Optional[User]:  # type: ignore
        return await self._model.objects.get_or_none(email=email)

    async def email_exists(self, email: str) -> bool:  # type: ignore
        return await self._model.objects.filter(email=email).exists()
