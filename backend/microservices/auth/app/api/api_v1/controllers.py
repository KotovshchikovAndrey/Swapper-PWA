# import typing as tp

from starlette.authentication import requires
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import Response

from database import postgres
from database.repositories.user import UserPostgreSQLRepository
from dto import token as token_dto
from dto import user as user_dto
from errors.exceptions.api import ApiError
from mixins.response import ResponseTokenPairMixin
from schemas import user as user_schema
from services import UserService
from utils.mapper import ApiMapper


class Registration(HTTPEndpoint, ResponseTokenPairMixin):
    __service = UserService(repository=UserPostgreSQLRepository())
    __mapper = ApiMapper(
        dto=user_dto.UserRegisterDTO, schema=user_schema.UserRegisterSchema()
    )

    @postgres.database.transaction()
    async def post(self, request: Request):
        dto = self.__mapper.convert_to_dto(await request.json())
        tokens = await self.__service.register(dto)

        return self._get_response(tokens, status=201)


class Login(HTTPEndpoint, ResponseTokenPairMixin):
    __service = UserService(repository=UserPostgreSQLRepository())
    __mapper = ApiMapper(
        dto=user_dto.UserLoginDTO, schema=user_schema.UserLoginSchema()
    )

    @postgres.database.transaction()
    async def post(self, request: Request):
        dto = self.__mapper.convert_to_dto(await request.json())
        tokens = await self.__service.login(dto)

        return self._get_response(tokens)


class Refresh(HTTPEndpoint, ResponseTokenPairMixin):
    __service = UserService(repository=UserPostgreSQLRepository())
    __mapper = ApiMapper(dto=token_dto.TokenUpdateDTO)

    @requires("authenticated")
    @postgres.database.transaction()
    async def patch(self, request: Request):
        refresh_token = self.__get_refresh_token_from_request(request)
        current_user = request.user

        dto = self.__mapper.convert_to_dto(
            {
                "user_id": current_user.id,
                "access_token": current_user.token,
                "refresh_token": refresh_token,
            }
        )
        new_tokens = await self.__service.refresh(dto)

        return self._get_response(new_tokens)

    def __get_refresh_token_from_request(self, request: Request):
        refresh_token = request.cookies.get("refresh_token", None)
        if refresh_token is None:
            raise ApiError.forbidden(message="Токен обновления не был получен!")

        return refresh_token


class Logout(HTTPEndpoint):
    __service = UserService(repository=UserPostgreSQLRepository())
    __mapper = ApiMapper(dto=user_dto.UserLogoutDTO)

    @requires("authenticated")
    async def delete(self, request: Request):
        refresh_token = self.__get_refresh_token_from_request(request)
        current_user = request.user

        dto = self.__mapper.convert_to_dto(
            {
                "id": current_user.id,
                "refresh_token": refresh_token,
            }
        )
        await self.__service.logout(dto)

        response = Response(status_code=204)
        response.delete_cookie("refresh_token")

        return response

    def __get_refresh_token_from_request(self, request: Request):
        refresh_token = request.cookies.get("refresh_token", None)
        if refresh_token is None:
            raise ApiError.forbidden(message="Токен обновления не был получен!")

        return refresh_token
