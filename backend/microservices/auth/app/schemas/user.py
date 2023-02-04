import typing as tp

from marshmallow import EXCLUDE, Schema, post_load

from dto.user import *
from schemas.custom_fields.fields import *


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

    @post_load
    def to_dto(self, data: tp.Dict[str, tp.Any], **kwargs: tp.Any):
        return UserRegisterDTO(**data)


class UserLoginSchema(Schema):
    email = EmailField(required=True, allow_none=False)
    password = PasswordField(required=True, allow_none=False)

    class Meta:
        unknown = EXCLUDE  # type: ignore

    @post_load
    def to_dto(self, data: tp.Dict[str, tp.Any], **kwargs: tp.Any):
        return UserLoginDTO(**data)
