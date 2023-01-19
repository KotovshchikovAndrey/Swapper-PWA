import typing as tp

from api.dependencies.requests_validators import UserRequestValidatorFactory
from fastapi.requests import Request

__all__ = ("UserRegistrationMiddleware",)


class UserRegistrationMiddleware:
    def __init__(self) -> None:
        self.__user_request_validator_factory = UserRequestValidatorFactory

    async def __call__(self, request: Request) -> tp.Any:
        validator = (
            self.__user_request_validator_factory.create_registration_validator()
        )
        await validator.validate(request)
