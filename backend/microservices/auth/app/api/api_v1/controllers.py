# import typing as tp

from starlette.authentication import requires
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import Response

from core.dependencies import injector
from database.connections import postgres_db

# from database.repositories.user import UserPostgreSQLRepository
from dto import token as token_dto
from dto import user as user_dto
from errors.exceptions.api import ApiError
from mixins.response import UserResponseMixin
from schemas import user as user_schema
from services.user import UserService
from utils.mapper import ApiMapper


class Registration(HTTPEndpoint, UserResponseMixin):
    mapper = ApiMapper(
        dto=user_dto.UserRegisterDTO,
        schema=user_schema.UserRegisterSchema(),
    )

    @injector.inject("UserService")
    @postgres_db.database.transaction()
    async def post(self, request: Request, service: UserService):
        dto = self.mapper.convert_to_dto(await request.json())
        user, access_token, refresh_token = await service.register(dto)

        return self.get_user_response(user, access_token, refresh_token, status=201)


class Login(HTTPEndpoint, UserResponseMixin):
    mapper = ApiMapper(
        dto=user_dto.UserLoginDTO,
        schema=user_schema.UserLoginSchema(),
    )

    @injector.inject("UserService")
    @postgres_db.database.transaction()
    async def post(self, request: Request, service: UserService):
        dto = self.mapper.convert_to_dto(await request.json())
        user, access_token, refresh_token = await service.login(dto)

        return self.get_user_response(user, access_token, refresh_token)


class Refresh(HTTPEndpoint, UserResponseMixin):
    mapper = ApiMapper(dto=token_dto.TokenUpdateDTO)

    @injector.inject("UserService")
    @postgres_db.database.transaction()
    @requires("authenticated")
    async def patch(self, request: Request, service: UserService):
        refresh_token = self.get_refresh_token_from_request(request)
        dto = self.mapper.convert_to_dto(
            {
                "user_id": request.user.id,
                "access_token": request.user.token,
                "refresh_token": refresh_token,
            }
        )

        user, access_token, refresh_token = await service.refresh(dto)

        return self.get_user_response(user, access_token, refresh_token)

    def get_refresh_token_from_request(self, request: Request):
        refresh_token = request.cookies.get("refresh_token", None)
        if refresh_token is None:
            raise ApiError.forbidden(message="Токен обновления не был получен!")

        return refresh_token


class Logout(HTTPEndpoint):
    mapper = ApiMapper(dto=user_dto.UserLogoutDTO)

    @injector.inject("UserService")
    @requires("authenticated")
    async def delete(self, request: Request, service: UserService):
        refresh_token = self.get_refresh_token_from_request(request)
        dto = self.mapper.convert_to_dto(
            {
                "id": request.user.id,
                "refresh_token": refresh_token,
            }
        )

        await service.logout(dto)

        response = Response(status_code=204)
        response.delete_cookie("refresh_token")

        return response

    def get_refresh_token_from_request(self, request: Request):
        refresh_token = request.cookies.get("refresh_token", None)
        if refresh_token is None:
            raise ApiError.forbidden(message="Токен обновления не был получен!")

        return refresh_token
