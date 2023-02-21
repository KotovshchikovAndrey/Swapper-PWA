import hashlib
import typing as tp

from utils.injector import injector
from core.entities import UserEntity
from core.interfaces.repositories import UserRepository
from dto.token import TokenUpdateDTO
from dto.user import *
from errors.exceptions.api import ApiError
from services.token import TokenService


class UserService:
    repository: UserRepository
    token_service: TokenService

    @injector.inject("UserRepository")  # type: ignore
    @injector.inject("TokenService")
    def __init__(
        self,
        repository: UserRepository,
        token_service: TokenService,
    ) -> None:
        self.repository = repository
        self.token_service = token_service

    async def register(self, dto: UserRegisterDTO) -> tp.Tuple[UserEntity, str, str]:
        email_exists = await self.repository.email_exists(email=dto.email)
        if email_exists:
            raise ApiError.bad_request("Пользователь с таким email уже существует!")

        password_hash = self.get_password_hash(password=dto.password)
        created_user = await self.repository.create(
            name=dto.name,
            email=dto.email,
            password=password_hash,
        )

        access_token, refresh_token = await self.get_token_pair(
            user=created_user,
            payload={
                "id": created_user.id,
                "name": created_user.name,
                "email": created_user.email,
            },
        )

        return created_user, access_token, refresh_token

    async def login(self, dto: UserLoginDTO) -> tp.Tuple[UserEntity, str, str]:
        user_in_db = await self.authenticate(email=dto.email, password=dto.password)
        if user_in_db is None:
            raise ApiError.unauthorized(message="Неверный логин или пароль")

        access_token, refresh_token = await self.get_token_pair(
            user=user_in_db,
            payload={
                "id": user_in_db.id,
                "name": user_in_db.name,
                "email": user_in_db.email,
            },
        )

        return user_in_db, access_token, refresh_token

    async def authenticate(self, email: str, password: str) -> tp.Optional[UserEntity]:
        user = await self.repository.find_by_email(email)
        if user is not None:
            password_hash = self.get_password_hash(password)
            if password_hash == user.password:
                return user

        return None

    async def refresh(self, dto: TokenUpdateDTO) -> tp.Tuple[UserEntity, str, str]:
        user = await self.repository.get_by_id(id=dto.user_id)
        if user is None:
            raise ApiError.not_found(message="Пользователь не найден!")

        new_access_token, new_refresh_token = await self.update_token_pair(
            user=user,
            access_token=dto.access_token,
            refresh_token=dto.refresh_token,
        )

        return user, new_access_token, new_refresh_token

    async def logout(self, dto: UserLogoutDTO) -> None:
        await self.token_service.remove_token_from_db(dto.id, dto.refresh_token)

    async def update_token_pair(
        self, user: UserEntity, access_token: str, refresh_token: str
    ) -> tp.Tuple[str, str]:
        payload = self.token_service.decode_refresh_token(
            refresh_token=refresh_token,
            access_token=access_token,
        )

        token_in_db = await self.token_service.check_token_in_db(
            user_id=user.id,
            token=refresh_token,
        )

        if not token_in_db:
            raise ApiError.forbidden(message="Невалидный токен!")

        return await self.token_service.update_token_pair(user, payload, refresh_token)

    async def get_token_pair(
        self, user: UserEntity, payload: tp.Dict[str, tp.Any]
    ) -> tp.Tuple[str, str]:
        access_token, refresh_token = await self.token_service.create_token_pair(
            user=user,
            payload=payload,
        )

        return access_token, refresh_token

    def get_password_hash(self, password: str):
        return hashlib.sha256(password.encode()).hexdigest()
