import typing as tp
from abc import ABC, abstractmethod

from dto.token import RefreshTokenDTO
from dto.user import LoginUserDTO, LogoutUserDTO, RegisterUserDTO
from errors.exceptions.api import ApiError
from services.token import ITokenService, get_token_service
from services.user import IUserService, get_user_service


class IAuthService(ABC):
    user_service: IUserService
    token_service: ITokenService

    @abstractmethod
    async def register(self, dto: RegisterUserDTO) -> tp.Tuple[str, str]:
        raise NotImplementedError()

    @abstractmethod
    async def login(self, dto: LoginUserDTO) -> tp.Tuple[str, str]:
        raise NotImplementedError()

    @abstractmethod
    async def refresh(self, dto: RefreshTokenDTO) -> tp.Tuple[str, str]:
        raise NotImplementedError()

    @abstractmethod
    async def logout(self, dto: LogoutUserDTO) -> None:
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

        new_user = await self.user_service.create_user(dto)
        token_payload = {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email,
        }

        access_token = self.token_service.generate_access_token(payload=token_payload)
        refresh_token = self.token_service.generate_refresh_token(
            access_token, payload=token_payload
        )

        await self.token_service.set_token(user=new_user, token=refresh_token)

        return access_token, refresh_token

    async def login(self, dto: LoginUserDTO):
        user = await self.user_service.authenticate(
            email=dto.email, password=dto.password
        )

        if user is None:
            raise ApiError.unauthorized(message="Неверный логин или пароль")

        token_payload = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
        }

        access_token = self.token_service.generate_access_token(payload=token_payload)
        refresh_token = self.token_service.generate_refresh_token(
            access_token, payload=token_payload
        )

        await self.token_service.set_token(user, token=refresh_token)

        return access_token, refresh_token

    async def refresh(self, dto: RefreshTokenDTO):
        token_payload = self.token_service.decode_refresh_token(
            refresh_token=dto.refresh_token,
            access_token=dto.access_token,
        )

        access_token = self.token_service.generate_access_token(payload=token_payload)
        refresh_token = self.token_service.generate_refresh_token(
            access_token=access_token,
            payload=token_payload,
        )

        await self.token_service.update_token(
            user=dto.user,
            token=dto.refresh_token,
            new_token=refresh_token,
        )

        return access_token, refresh_token

    async def logout(self, dto: LogoutUserDTO):
        await self.token_service.remove_token(user=dto.user, token=dto.token)
        return None


# Current AuthService implementation for import
auth_service = AuthService()


def get_auth_service(use_cache: bool = True) -> IAuthService:
    if use_cache:
        return auth_service

    return AuthService()
