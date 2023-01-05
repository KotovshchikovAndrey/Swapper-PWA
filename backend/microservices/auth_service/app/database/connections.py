from __future__ import annotations

import typing as tp

import databases
import sqlalchemy

__all__ = ("postgresql_connection",)


class PostgreSQLConnection:
    __instance: tp.Optional[PostgreSQLConnection] = None
    __metadata: sqlalchemy.MetaData
    __database: databases.Database

    user: str
    password: str
    db_name: str
    host: str
    port: tp.Union[str, int]

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(
        self,
        user: str,
        password: str,
        db_name: str,
        host: str,
        port: tp.Union[str, int],
    ) -> None:
        self.user = user
        self.password = password
        self.db_name = db_name

        self.host = host
        self.port = port

        self.__metadata = sqlalchemy.MetaData()
        self.__database = databases.Database(url=self.db_url)

    async def connect(self):
        await self.database.connect()

    async def disconnect(self):
        database = self.database
        if database.is_connected:
            await self.database.disconnect()

    @property
    def db_url(self):
        return f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"

    @property
    def metadata(self):
        return self.__metadata

    @property
    def database(self):
        return self.__database


postgresql_connection = PostgreSQLConnection(
    user="postgres",
    password="12345",
    db_name="test_auth_db",
    host="127.0.0.1",
    port=5432,
)
