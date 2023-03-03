from __future__ import annotations

import typing as tp

from database.connections.base import SQLConnection


class PostgreSQLConnection(SQLConnection):
    __instance: tp.Optional[PostgreSQLConnection] = None

    user: str
    password: str
    db_name: str
    host: str
    port: tp.Union[str, int]

    def __new__(cls, *args: tp.Any, **kwargs: tp.Any):
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

        super().__init__(url=self.get_url())

    def get_url(self):
        return f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"
