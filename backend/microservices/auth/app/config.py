import os

from dotenv import load_dotenv

from errors.config import ConfigError


class AppConfig:
    @staticmethod
    def load_env_config(path: str = ".env"):
        load_dotenv(path)

    @staticmethod
    def get_secret_key():
        SECRET_KEY = os.getenv("SECRET_KEY")
        if SECRET_KEY is None:
            raise ConfigError(
                message="Константа SECRET_KEY не определена в переменном окружении"
            )

        return SECRET_KEY

    @staticmethod
    def get_postgres_config():
        POSTGRES_USER = os.getenv("POSTGRES_USER")
        POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
        POSTGRES_DB_NAME = os.getenv("POSTGRES_DB_NAME")
        POSTGRES_HOST = os.getenv("POSTGRES_HOST")
        POSTGRES_PORT = os.getenv("POSTGRES_PORT")

        if (
            POSTGRES_USER is None
            or POSTGRES_PASSWORD is None
            or POSTGRES_DB_NAME is None
            or POSTGRES_HOST is None
            or POSTGRES_PORT is None
        ):
            raise ConfigError(
                message="""
                        Неверная конфигурация postgres!
                        Константы POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB_NAME, POSTGRES_HOST, POSTGRES_PORT 
                        не были получены из переменного окружения!
                    """
            )

        return {
            "user": POSTGRES_USER,
            "password": POSTGRES_PASSWORD,
            "db_name": POSTGRES_DB_NAME,
            "host": POSTGRES_HOST,
            "port": POSTGRES_PORT,
        }
