import hashlib
import typing as tp

from database.entities import UserEntity
from database.repositories import UserRepository
from database.repositories.token import TokenPostgreSQLRepository
from domain.services import TokenService
from dto.user import *
from errors.api import ApiError

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
        created_user = await self.__repository.create(
            name=user.name,
            surname=user.surname,
            email=user.email,
            age=user.age,
            patronymic=user.patronymic,
            phone=user.phone,
            password=password_hash,
        )

        access_token, refresh_token = await self.__get_token_pair(
            user=created_user,
            payload={
                "id": created_user.id,
                "name": created_user.name,
            },
        )

        return access_token, refresh_token

    async def login(self, user: UserLoginDTO) -> tp.Tuple[str, str]:
        user = await self.authenticate(email=user.email, password=user.password)
        if user is None:
            raise ApiError.unauthorized(message="Неверный логин или пароль")

        access_token, refresh_token = await self.__get_token_pair(
            user=user,
            payload={
                "id": user.id,
                "name": user.name,
            },
        )

        return access_token, refresh_token

    async def logout(self, user_id: int, token: str) -> None:
        token_service = TokenService(repository=TokenPostgreSQLRepository())
        await token_service.remove_token_from_db(user_id, token)

    async def refresh_tokens(
        self, access_token: str, refresh_token: str
    ) -> tp.Tuple[str, str]:

        pass

    async def authenticate(
        self, email: str, password: str
    ) -> tp.Union[None, UserEntity]:
        user = await self.__repository.find_by_email(email)
        if user is not None:
            password_hash = self.__get_password_hash(password)
            if password_hash == user.password:
                return user

        return None

    async def __get_token_pair(
        self, user: UserEntity, payload: dict
    ) -> tp.Tuple[str, str]:
        token_service = TokenService(repository=TokenPostgreSQLRepository())
        access_token, refresh_token = await token_service.create_token_pair(
            user=user, payload=payload
        )

        return access_token, refresh_token

    def __get_password_hash(self, password: str):
        # Мб соль добавить
        return hashlib.sha256(password.encode()).hexdigest()
