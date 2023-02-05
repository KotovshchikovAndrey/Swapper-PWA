# import typing as tp

from marshmallow import EXCLUDE, Schema

from dto.user import *
from schemas.fields import *


class UserRegisterSchema(Schema):
    name = NameField(required=True, allow_none=False)
    surname = SurnameField(required=True, allow_none=False)
    age = AgeField(required=True, allow_none=False)
    email = EmailField(required=True, allow_none=False)
    password = PasswordField(required=True, allow_none=False)
    patronymic = PatronymicField(allow_none=False)
    phone = PhoneField(allow_none=False)

    class Meta:
        unknown = EXCLUDE  # type: ignore


class UserLoginSchema(Schema):
    email = EmailField(required=True, allow_none=False)
    password = PasswordField(required=True, allow_none=False)

    class Meta:
        unknown = EXCLUDE  # type: ignore
