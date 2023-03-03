import typing as tp
from abc import ABC, abstractmethod

from core.entities import IUser

from services.user import IUserService, get_user_service
from services.token import ITokenService, get_token_service

from dto.user import RegisterUserDTO, UserLoginDTO, UserLogoutDTO
from dto.token import TokenUpdateDTO
from errors.exceptions.api import ApiError

service = None


class IAuthService(ABC):
    user_service: IUserService
    token_service: ITokenService

    @abstractmethod
    async def register(self, dto: RegisterUserDTO) -> tp.Tuple[IUser, str, str]:
        raise NotImplementedError()

    @abstractmethod
    async def login(self, dto) -> tp.Tuple[IUser, str, str]:
        raise NotImplementedError()

    @abstractmethod
    async def refresh(self, dto) -> tp.Tuple[IUser, str, str]:
        raise NotImplementedError()

    @abstractmethod
    async def logout(self, dto) -> None:
        raise NotImplementedError()


class AuthService(IAuthService):
    def __init__(
        self,
        user_service: IUserService = get_user_service(),
        token_service: ITokenService = get_token_service(),
    ) -> None:
        self.user_service = user_service
        self.token_service = token_service

    async def register(self, dto: RegisterUserDTO):
        is_user_exists = await self.user_service.check_user_exists(email=dto.email)
        if is_user_exists:
            raise ApiError.bad_request("Пользователь с таким email уже существует!")

        new_user = self.user_service.create_user(dto)
        token_payload = {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email,
        }

        access_token = await self.token_service.generate_access_token(
            payload=token_payload
        )
        refresh_token = self.token_service.generate_refresh_token(
            access_token, payload=token_payload
        )

        return new_user, access_token, refresh_token

    async def login(self, dto: UserLoginDTO) -> tp.Tuple[IUser, str, str]:
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

    async def refresh(self, dto: TokenUpdateDTO) -> tp.Tuple[IUser, str, str]:
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


# Current AuthService implementation for import
def get_auth_service(use_cache: bool = True) -> IAuthService:
    if (service is not None) and use_cache:
        return service

    return AuthService()

    # async def update_token_pair(
    #     self, user: UserEntity, access_token: str, refresh_token: str
    # ) -> tp.Tuple[str, str]:
    #     payload = self.token_service.decode_refresh_token(
    #         refresh_token=refresh_token,
    #         access_token=access_token,
    #     )

    #     token_in_db = await self.token_service.check_token_in_db(
    #         user_id=user.id,
    #         token=refresh_token,
    #     )

    #     if not token_in_db:
    #         raise ApiError.forbidden(message="Невалидный токен!")

    #     return await self.token_service.update_token_pair(user, payload, refresh_token)
