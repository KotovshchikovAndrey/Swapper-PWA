import hashlib
import typing as tp

from database.repositories import UserRepository
from dto.user_dto import *
from errors.api_errors import ApiError

__all__ = ("UserService",)


class UserService:
    __repository: UserRepository

    def __init__(self, repository: UserRepository) -> None:
        self.__repository = repository

    async def register(self, user: UserRegisterDTO):
        email_exists = await self.__repository.email_exists(email=user.email)
        if email_exists:
            raise ApiError.bad_request("Пользователь с таким email уже существует!")

        password_hash = self.__get_password_hash(password=user.password)
        print(password_hash)

    async def login(self, user: UserLoginDTO):
        pass

    def __get_password_hash(self, password: str):
        # Мб соль добавить
        return hashlib.sha256(password.encode()).hexdigest()
