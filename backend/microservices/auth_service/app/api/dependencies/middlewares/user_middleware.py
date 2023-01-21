import typing as tp

from fastapi.requests import Request

from api.dependencies.requests_validators import (RequestValidator,
                                                  UserRequestValidatorFactory)

__all__ = ("UserMiddleware",)


class UserMiddleware:
    @staticmethod
    async def validate_registration_request(request: Request):
        request_validator = UserRequestValidatorFactory.create_registration_validator()
        await request_validator.validate(request)
