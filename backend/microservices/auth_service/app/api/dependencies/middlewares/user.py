import typing as tp

from fastapi.requests import Request

from api.dependencies.request_validators import UserRequestValidatorFactory

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
