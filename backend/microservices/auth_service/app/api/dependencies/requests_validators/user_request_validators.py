import typing as tp

from fastapi.requests import Request

from api.dependencies.requests_validators.base_request_validator import \
    RequestValidator
from dto.user_dto import UserRegisterDTO
from errors.api_errors import ApiError

__all__ = ("UserRequestValidatorFactory",)


class UserRegistrationValidator(RequestValidator):
    def __init__(self) -> None:
        super().__init__()

    async def validate(self, request: Request) -> tp.Union[UserRegisterDTO, ApiError]:
        user_data: dict = await request.json()
        name, surname, email = (
            user_data.get("name"),
            user_data.get("surname"),
            user_data.get("email"),
        )

        self.__validate_name(name)
        self.__validate_surname(surname)
        self.__validate_email(email)

        if self._errors:
            raise ApiError.bad_request(
                message="Невалидные пользовательские данные", details=self._errors
            )

    def __validate_name(self, name: tp.Optional[str]):
        if name is None:
            self._errors.append("Введите свое имя")

    def __validate_surname(self, surname: tp.Optional[str]):
        if surname is None:
            self._errors.append("Введите свою фамилию")

    def __validate_email(self, email: tp.Optional[str]):
        if email is None:
            self._errors.append("Введите свой email")


class UserRequestValidatorFactory:
    @staticmethod
    def create_registration_validator():
        return UserRegistrationValidator()
