# import typing as tp

from starlette.authentication import requires
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import Response

from database.connections import transaction

from dto import token as token_dto
from dto import user as user_dto

from errors.exceptions.api import ApiError

from mixins.response import TokenResponseMixin
from schemas import user as user_schema
from utils.mapper import ApiMapper

from services.auth import get_auth_service


class Registration(HTTPEndpoint, TokenResponseMixin):
    service = get_auth_service()
    mapper = ApiMapper(
        dto=user_dto.RegisterUserDTO,
        schema=user_schema.UserRegisterSchema(),
    )

    @transaction
    async def post(self, request: Request):
        dto = self.mapper.convert_to_dto(await request.json())
        access_token, refresh_token = await self.service.register(dto)

        return self.get_response(access_token, refresh_token, status=201)


class Login(HTTPEndpoint, TokenResponseMixin):
    service = get_auth_service()
    mapper = ApiMapper(
        dto=user_dto.LoginUserDTO,
        schema=user_schema.UserLoginSchema(),
    )

    @transaction
    async def post(self, request: Request):
        dto = self.mapper.convert_to_dto(await request.json())
        access_token, refresh_token = await self.service.login(dto)

        return self.get_response(access_token, refresh_token)


class Refresh(HTTPEndpoint, TokenResponseMixin):
    service = get_auth_service()
    mapper = ApiMapper(dto=token_dto.RefreshTokenDTO)

    @transaction
    @requires("authenticated")
    async def patch(self, request: Request):
        current_user = request.user.instance
        access_token = request.user.token
        refresh_token = self.get_token_from_cookie(request)

        convert_data = {
            "user": current_user,
            "access_token": access_token,
            "refresh_token": refresh_token,
        }

        dto = self.mapper.convert_to_dto(data=convert_data)
        access_token, refresh_token = await self.service.refresh(dto)

        return self.get_response(access_token, refresh_token)

    def get_token_from_cookie(self, request: Request):
        token = request.cookies.get("refresh_token", None)
        if token is None:
            raise ApiError.forbidden(message="Токен обновления не был получен!")

        return token


class Logout(HTTPEndpoint):
    service = get_auth_service()
    mapper = ApiMapper(dto=user_dto.LogoutUserDTO)

    @requires("authenticated")
    async def delete(self, request: Request):
        current_user = request.user.instance
        refresh_token = self.get_token_from_cookie(request)

        convert_data = {
            "user": current_user,
            "token": refresh_token,
        }

        dto = self.mapper.convert_to_dto(data=convert_data)
        await self.service.logout(dto)

        response = Response(status_code=204)
        response.delete_cookie("refresh_token")

        return response

    def get_token_from_cookie(self, request: Request):
        token = request.cookies.get("refresh_token", None)
        if token is None:
            raise ApiError.forbidden(message="Токен обновления не был получен!")

        return token
