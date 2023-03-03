import hashlib
import typing as tp

from core.entities import IUser
from database.repositories.user import IUserRepository
from dto.user import RegisterUserDTO
from errors.exceptions.api import ApiError

from abc import ABC, abstractmethod

service = None


class IUserService(ABC):
    @abstractmethod
    async def create_user(self, dto: RegisterUserDTO) -> IUser:
        raise NotImplementedError()

    async def check_user_exists(self, email: str) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def authenticate(self, email: str, password: str) -> tp.Optional[IUser]:
        raise NotImplementedError()

    @abstractmethod
    def get_password_hash(self, password: str) -> str:
        raise NotImplementedError()


class UserService(IUserService):
    repository: IUserRepository

    def __init__(self, repository: IUserRepository):
        self.repository = repository

    async def check_user_exists(self, email: str):
        user = self.repository.find_by_email(email=email)
        if user is not None:
            return True

        return False

    async def authenticate(self, email: str, password: str):
        user = await self.repository.find_by_email(email)
        if user is not None:
            password_hash = self.get_password_hash(password)
            if password_hash == user.password:
                return user

        return None

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


# Current UserService implementation for import
def get_user_service(use_cache: bool = True) -> IUserService:
    if (service is not None) and use_cache:
        return service

    return UserService()
