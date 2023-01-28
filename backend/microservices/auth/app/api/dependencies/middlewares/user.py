from fastapi.requests import Request

from api.dependencies.auth_backend import JwtAuthBackend
from api.dependencies.request_validators import UserRequestValidatorFactory
from database.repositories.token import TokenPostgreSQLRepository
from domain.services import TokenService

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
    async def check_can_refresh(request: Request):
        jwt_auth_backend = JwtAuthBackend(
            service=TokenService(repository=TokenPostgreSQLRepository())
        )
        payload = await jwt_auth_backend.check_refresh_token(request)
        setattr(request, "user_payload", payload)
