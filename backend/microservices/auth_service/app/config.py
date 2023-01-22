import os
import typing as tp

from errors.config_errors import ConfigError


class AppConfig:
    @staticmethod
    def get_secret_key():
        SECRET_KEY = os.getenv("SECRET_KEY")
        if SECRET_KEY is None:
            raise ConfigError(
                message="Константа SECRET_KEY не определена в переменном окружении"
            )

        return SECRET_KEY
