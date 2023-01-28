import typing as tp

from validate_email import validate_email as email_is_valid  # type: ignore

from api.dependencies.request_validators.base import RequestValidator
from domain.mappers import UserMapper
from dto.user import UserLoginDTO, UserRegisterDTO

__all__ = ("UserRequestValidatorFactory",)


class UserValidator(RequestValidator):
    def __init__(self, dto_cls: tp.Type[object]) -> None:
        super().__init__(fields=UserMapper.get_fields(dto_cls))

    def validate_email(self, email: tp.Optional[str]):
        if email is None:
            self._errors.append("Введите свой email")

        elif len(email) > 100:
            self._errors.append("Введенный email не должен превышать 100 сиволов")

        elif not email_is_valid(email):
            self._errors.append("Введите корректный email адресс")

    def validate_password(self, password: tp.Optional[str]):
        if not password:
            self._errors.append("Пароль не может быть пустой строкой")


class UserRegistrationValidator(UserValidator):
    def __init__(self) -> None:
        super().__init__(dto_cls=UserRegisterDTO)

    def validate_name(self, name: tp.Any):
        if name is None:
            self._errors.append("Введите свое имя")

        elif not isinstance(name, str):
            self._errors.append("Поле name должно быть строкой!")

        elif len(name) > 100:
            self._errors.append("Имя не должно превышать 100 символов")

    def validate_surname(self, surname: tp.Any):
        if surname is None:
            self._errors.append("Введите свою фамилию")

        elif not isinstance(surname, str):
            self._errors.append("Поле surname должно быть строкой!")

        elif len(surname) > 100:
            self._errors.append("Фамилия не должна превышать 100 символов")

    def validate_age(self, age: tp.Any):
        if age is None:
            self._errors.append("Введите свой возраст")

        elif not isinstance(age, int):
            self._errors.append("Поле age должно быть числом!")

        elif not (1 <= age <= 100):
            self._errors.append("Возраст должен быть числом от 1 до 100")

    def validate_patronymic(self, patronymic: tp.Any):
        if patronymic is None:
            return

        if not isinstance(patronymic, str):
            self._errors.append("Поле patronymic должно быть строкой!")

        elif len(patronymic) > 100:
            self._errors.append("Отчество не должно превышать 100 сиволов в длину")

    def validate_phone(self, phone: tp.Any):
        if phone is None:
            return

        if not isinstance(phone, str):
            self._errors.append("Поле phone должно быть строкой!")

        elif len(phone) > 18:
            self._errors.append(
                "Номер телефона не должен превышать 18 символов в длину"
            )


class UserLoginValidator(UserValidator):
    def __init__(self) -> None:
        super().__init__(dto_cls=UserLoginDTO)

    def validate_confirm_password(self, confirm_password: tp.Any):
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
