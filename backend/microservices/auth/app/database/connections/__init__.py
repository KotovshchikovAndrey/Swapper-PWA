from .factory import DatabaseConnectionFactory

db_connection_factory = DatabaseConnectionFactory()

postgres_db = db_connection_factory.get_connection(database="postgres")
