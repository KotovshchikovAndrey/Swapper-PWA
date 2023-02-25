import typing as tp

from marshmallow import fields
from marshmallow.validate import Length
from marshmallow.exceptions import ValidationError

from utils.validators import *


class NameField(fields.String):
    default_error_messages = {
        "null": "Поле name не может быть пустым!",
        "required": "Поле name обязательно для заполнения!",
        "invalid": "Поле name должно быть строкой!",
    }

    def _deserialize(self, value: str, *args: tp.Any, **kwargs: tp.Any):
        validate_name_length = Length(
            min=1,
            max=100,
            error="Поле name должно быть длиной от 1 до 100 символов",
        )
        validate_name_length(value)

        return value


class SurnameField(fields.String):
    default_error_messages = {
        "null": "Поле surname не может быть пустым!",
        "required": "Поле surname обязательно для заполнения!",
        "invalid": "Поле surname должно быть строкой!",
    }

    def _deserialize(self, value: str, *args: tp.Any, **kwargs: tp.Any):
        validate_surname_length = Length(
            min=1,
            max=100,
            error="Поле surname не должно превышать 100 символов!",
        )
        validate_surname_length(value)

        return value


class AgeField(fields.Integer):
    default_error_messages = {
        "null": "Поле age не может быть пустым!",
        "required": "Поле age обязательно для заполнения!",
        "invalid": "Поле age должно целым положительным быть числом!",
    }

    def _deserialize(self, value: int, *args: tp.Any, **kwargs: tp.Any):
        valiadator = RangeValidator((1, 100))
        is_valid = valiadator.validate(value)
        if not is_valid:
            raise ValidationError("Поле age должно быть числом от 1 до 100!")

        return value


class EmailField(fields.Email):
    default_error_messages = {
        "null": "Поле email не может быть пустым!",
        "required": "Поле email обязательно для заполнения!",
        "invalid": "Некорректный email адрес!",
    }

    def _deserialize(self, value: str, *args: tp.Any, **kwargs: tp.Any):
        valiadator = MaxLengthValidator(100)
        is_valid = valiadator.validate(value)
        if not is_valid:
            raise ValidationError("Поле email не должно превышать 100 символов!")

        return value


class PasswordField(fields.String):
    default_error_messages = {
        "null": "Поле password не может быть пустым!",
        "required": "Поле password обязательно для заполнения!",
        "invalid": "Поле password должно быть строкой!",
    }

    def _deserialize(self, value: str, *args: tp.Any, **kwargs: tp.Any):
        valiadator = MaxLengthValidator(255)
        is_valid = valiadator.validate(value)
        if not is_valid:
            raise ValidationError("Поле password не должно превышать 255 символов!")

        return value


class PatronymicField(fields.String):
    default_error_messages = {
        "null": "Поле patronymic не может быть пустым!",
        "invalid": "Поле patronymic должно быть строкой!",
    }

    def _deserialize(self, value: str, *args: tp.Any, **kwargs: tp.Any):
        valiadator = MaxLengthValidator(100)
        is_valid = valiadator.validate(value)
        if not is_valid:
            raise ValidationError("Поле patronymic не должно превышать 100 символов!")

        return value


class PhoneField(fields.String):
    default_error_messages = {
        "null": "Поле phone не может быть пустым!",
        "invalid": "Поле phone должно быть строкой!",
    }

    def _deserialize(self, value: str, *args: tp.Any, **kwargs: tp.Any):
        valiadator = MaxLengthValidator(18)
        is_valid = valiadator.validate(value)
        if not is_valid:
            raise ValidationError("Поле phone не должно превышать 18 символов!")

        return value
