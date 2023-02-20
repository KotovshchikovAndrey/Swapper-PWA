import typing as tp

from core.interfaces.repositories import TokenRepository
from database.connections.postgres import PostgreSQLConnection
from database.models import Token, User
from database.repositories.base import BaseSqlRepository


class TokenPostgreSQLRepository(BaseSqlRepository[Token], TokenRepository):
    __db_connection: PostgreSQLConnection

    def __init__(self, db_connection: PostgreSQLConnection) -> None:
        super().__init__(model=Token)
        self.__db_connection = db_connection

    async def create(self, user_instance: User, value: str) -> None:  # type: ignore
        await self._model.objects.create(user=user_instance, value=value)

    async def update(self, user_instance: User, old_value: str, new_value: str) -> None:  # type: ignore
        token = await self._model.objects.get(user=user_instance, value=old_value)
        token.value = new_value  # type: ignore
        await token.update()

    async def delete(self, user_id: int, token: str) -> None:
        await self._model.objects.delete(user__id=user_id, value=token)

    async def find_by_user_id_and_value(  # type: ignore
        self, user_id: int, value: str
    ) -> tp.Optional[Token]:
        return await self._model.objects.get_or_none(user__id=user_id, value=value)
