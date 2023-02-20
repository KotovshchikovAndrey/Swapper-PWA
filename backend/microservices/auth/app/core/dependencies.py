# import typing as tp
from database.connections import postgres_db
from database.repositories.token import TokenPostgreSQLRepository
from database.repositories.user import UserPostgreSQLRepository
from utils.injector import Injector

__all__ = ("injector",)

dependencies = {
    "UserRepository": UserPostgreSQLRepository(db_connection=postgres_db),
    "TokenRepository": TokenPostgreSQLRepository(db_connection=postgres_db),
}

injector = Injector(dependencies)
