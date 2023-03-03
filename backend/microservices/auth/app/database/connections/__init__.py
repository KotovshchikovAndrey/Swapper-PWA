from core import config
from .base import SQLConnection
from .postgres import PostgreSQLConnection


def get_connection() -> SQLConnection:
    return PostgreSQLConnection(
        user=config.POSTGRES_USER,  # type: ignore
        password=config.POSTGRES_PASSWORD,  # type: ignore
        db_name=config.POSTGRES_DB_NAME,  # type: ignore
        host=config.POSTGRES_HOST,  # type: ignore
        port=config.POSTGRES_PORT,  # type: ignore
    )
