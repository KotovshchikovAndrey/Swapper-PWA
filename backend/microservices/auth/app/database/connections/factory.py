# import typing as tp

from database.connections.postgres import PostgreSQLConnection


class DatabaseConnectionFactory:
    def __init__(self) -> None:
        self.database_connections = {
            "postgres": PostgreSQLConnection,
        }

    def get_connection(self, database: str):
        return self.database_connections[database].get_connection()
