import typing as tp

from fastapi.requests import Request

from api.dependencies.request_validators import UserRequestValidatorFactory
from api.dependencies.auth_backend import JwtAuthBackend
from domain.services import TokenService
from database.repositories.token import TokenPostgreSQLRepository

__all__ = ("UserMiddleware",)


class UserMiddleware:
    @staticmethod
    async def validate_registration_request(request: Request):
        request_validator = UserRequestValidatorFactory.create_registration_validator()
        await request_validator.validate(request)

    @staticmethod
    async def validate_login_request(request: Request):
        request_validator = UserRequestValidatorFactory.create_login_validator()
        await request_validator.validate(request)

    @staticmethod
    def check_auth(request: Request):
        jwt_auth_backend = JwtAuthBackend(
            service=TokenService(repository=TokenPostgreSQLRepository())
        )
        payload = jwt_auth_backend.check_access_token(request)
        setattr(request, "user_payload", payload)

    @staticmethod
    def check_can_refresh(request: Request):
        jwt_auth_backend = JwtAuthBackend(
            service=TokenService(repository=TokenPostgreSQLRepository())
        )
        jwt_auth_backend.check_refresh_token(request)
