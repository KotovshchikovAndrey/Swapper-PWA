import typing as tp
from dataclasses import fields

from fastapi.requests import Request
from validate_email import validate_email

from api.dependencies.requests_validators.base_request_validator import RequestValidator
from domain.mappers import UserMapper
from dto.user_dto import UserLoginDTO, UserRegisterDTO
from errors.api_errors import ApiError

__all__ = ("UserRequestValidatorFactory",)


class UserValidator(RequestValidator):
    def __init__(self, dto_cls: tp.Type) -> None:
        super().__init__(fields=UserMapper.get_fields(dto_cls))

    def validate_email(self, email: tp.Optional[str]):
        if email is None:
            self._errors.append("Введите свой email")
            return

        if len(email) > 100:
            self._errors.append("Введенный email не должен превышать 100 сиволов")

        if not validate_email(email):
            self._errors.append("Введите корректный email адресс")

    def validate_password(self, password: tp.Optional[str]):
        if not password:
            self._errors.append("Пароль не может быть пустой строкой")


class UserRegistrationValidator(UserValidator):
    def __init__(self) -> None:
        super().__init__(dto_cls=UserRegisterDTO)

    def validate_name(self, name: tp.Optional[str]):
        if name is None:
            self._errors.append("Введите свое имя")
            return

        if len(name) > 100:
            self._errors.append("Имя не должно превышать 100 символов")

    def validate_surname(self, surname: tp.Optional[str]):
        if surname is None:
            self._errors.append("Введите свою фамилию")
            return

        if len(surname) > 100:
            self._errors.append("Фамилия не должна превышать 100 символов")

    def validate_age(self, age: tp.Optional[int]):
        if age is None:
            self._errors.append("Введите свой возраст")
            return

        if not isinstance(age, int) or not (1 <= age <= 100):
            self._errors.append("Введите корректный возраст")

    def validate_patronymic(self, patronymic: tp.Optional[str]):
        if (patronymic is not None) and (len(patronymic) > 100):
            self._errors.append("Отчество не должно превышать 100 сиволов")

    def validate_phone(self, phone: tp.Optional[str]):
        if (phone is not None) and (len(phone) > 18):
            self._errors.append("Номер телефона не должен превышать 18 символов")


class UserLoginValidator(UserValidator):
    def __init__(self) -> None:
        super().__init__(dto_cls=UserLoginDTO)

    def validate_confirm_password(self, confirm_password: tp.Optional[str]):
        password = self._valid_data.get("password")
        if password != confirm_password:
            self._errors.append("Пароли не совпадают")


class UserRequestValidatorFactory:
    @staticmethod
    def create_registration_validator():
        return UserRegistrationValidator()

    @staticmethod
    def create_login_validator():
        return UserLoginValidator()
