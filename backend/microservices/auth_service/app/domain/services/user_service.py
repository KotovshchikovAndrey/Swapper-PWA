import hashlib
import typing as tp

from database.models import User
from database.repositories import UserRepository
from database.repositories.token_repositories import TokenPostgreSQLRepository
from domain.services import TokenService
from dto.user_dto import *
from errors.api_errors import ApiError

__all__ = ("UserService",)


class UserService:
    __repository: UserRepository

    def __init__(self, repository: UserRepository) -> None:
        self.__repository = repository

    async def register(self, user: UserRegisterDTO) -> tp.Tuple[str, str]:
        email_exists = await self.__repository.email_exists(email=user.email)
        if email_exists:
            raise ApiError.bad_request("Пользователь с таким email уже существует!")

        password_hash = self.__get_password_hash(password=user.password)
        created_user: User = await self.__repository.create(
            name=user.name,
            surname=user.surname,
            email=user.email,
            age=user.age,
            patronymic=user.patronymic,
            phone=user.phone,
            password=password_hash,
        )
        payload = {
            "id": created_user.id,
            "name": created_user.name,
        }

        token_service = TokenService(repository=TokenPostgreSQLRepository())
        access_token, refresh_token = await token_service.create_tokens_for_user(
            user=created_user, payload=payload
        )

        return access_token, refresh_token

    async def login(self, user: UserLoginDTO):
        pass

    def __get_password_hash(self, password: str):
        # Мб соль добавить
        return hashlib.sha256(password.encode()).hexdigest()
