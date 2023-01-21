import typing as tp

from database.repositories.user_repositories import UserRepository
from dto.user_dto import *


class UserService:
    __repository: UserRepository

    def __init__(self, repository: UserRepository) -> None:
        self.__repository = repository

    async def register(self, user: UserRegisterDTO):
        pass

    async def login(self, user: UserLoginDTO):
        pass
