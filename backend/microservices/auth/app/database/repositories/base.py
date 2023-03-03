from abc import ABC

from database.connections import get_connection
from database.connections.base import SQLConnection


class SQLRepository(ABC):
    database: SQLConnection

    def __init__(self, db_connection: SQLConnection = get_connection()):
        self.database = db_connection
