import typing as tp

from database.repositories import TokenRepository

__all__ = ("TokenService",)


class TokenService:
    def __init__(self, repository: TokenRepository) -> None:
        self.__repository = repository
