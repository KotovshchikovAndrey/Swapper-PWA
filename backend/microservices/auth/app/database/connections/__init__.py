from core import config
from .base import SQLConnection
from .postgres import PostgreSQLConnection

connection = PostgreSQLConnection(
    user=config.POSTGRES_USER,  # type: ignore
    password=config.POSTGRES_PASSWORD,  # type: ignore
    db_name=config.POSTGRES_DB_NAME,  # type: ignore
    host=config.POSTGRES_HOST,  # type: ignore
    port=config.POSTGRES_PORT,  # type: ignore
)


def get_connection() -> SQLConnection:
    return connection


transaction = get_connection().database.transaction()
