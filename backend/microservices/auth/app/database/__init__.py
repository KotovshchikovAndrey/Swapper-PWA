from . import connections

postgres = connections.PostgreSQLConnection.get_connection()
