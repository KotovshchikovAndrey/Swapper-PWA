from __future__ import annotations

from abc import ABC, abstractmethod

import databases
import sqlalchemy


class DatabaseConnection(ABC):
    @abstractmethod
    async def connect(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def disconnect(self) -> None:
        raise NotImplementedError()


class SQLConnection(DatabaseConnection):
    __metadata: sqlalchemy.MetaData
    __database: databases.Database

    def __init__(self, url: str) -> None:
        self.__metadata = sqlalchemy.MetaData()
        self.__database = databases.Database(url=url)

    async def connect(self):
        await self.database.connect()

    async def disconnect(self):
        database = self.database
        if database.is_connected:
            await self.database.disconnect()

    @property
    def metadata(self):
        return self.__metadata

    @property
    def database(self):
        return self.__database
