from database.connections.base import SQLConnection
from database.connections import get_connection
from abc import ABC


class SQLRepository(ABC):
    database: SQLConnection

    def __init__(self, db_connection: SQLConnection = get_connection()):
        self.database = db_connection
