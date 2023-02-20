import typing as tp

from core.interfaces.repositories import UserRepository
from database.connections.postgres import PostgreSQLConnection
from database.models import User
from database.repositories.base import BaseSqlRepository


class UserPostgreSQLRepository(BaseSqlRepository[User], UserRepository):
    __db_connection: PostgreSQLConnection

    def __init__(self, db_connection: PostgreSQLConnection) -> None:
        super().__init__(model=User)
        self.__db_connection = db_connection

    async def get_by_id(self, id: tp.Union[int, str]) -> tp.Optional[User]:  # type: ignore
        return await super().get_by_id(id=id)

    async def create(  # type: ignore
        self,
        name: str,
        email: str,
        password: str,
        phone: tp.Optional[str] = None,
    ) -> User:
        created_user = await self._model.objects.create(
            name=name,
            email=email,
            phone=phone,
            password=password,
        )

        return created_user

    async def find_by_email(self, email: str) -> tp.Optional[User]:  # type: ignore
        return await self._model.objects.get_or_none(email=email)

    async def email_exists(self, email: str) -> bool:  # type: ignore
        return await self._model.objects.filter(email=email).exists()
