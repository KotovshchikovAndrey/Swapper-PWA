import hashlib
import typing as tp
from abc import ABC, abstractmethod

from core.entities import IUser
from database.repositories.user import IUserRepository, get_user_repository
from dto.user import RegisterUserDTO

service = None


class IUserService(ABC):
    repository: IUserRepository

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
    def __init__(self, repository: IUserRepository = get_user_repository()):
        self.repository = repository

    async def create_user(self, dto: RegisterUserDTO):
        password_hash = self.get_password_hash(password=dto.password)
        new_user = await self.repository.create(
            name=dto.name,
            email=dto.email,
            password=password_hash,
            phone=dto.phone,
        )

        return new_user

    async def check_user_exists(self, email: str):
        user = await self.repository.find_by_email(email=email)
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

    def get_password_hash(self, password: str):
        return hashlib.sha256(password.encode()).hexdigest()


# Current UserService implementation for import
def get_user_service(use_cache: bool = True) -> IUserService:
    if (service is not None) and use_cache:
        return service

    return UserService()
