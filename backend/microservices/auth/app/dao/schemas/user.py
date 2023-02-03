import typing as tp

from marshmallow import Schema, post_load

from dao.schemas.custom_fields.fields import *
from dto.user import *


class UserRegisterSchema(Schema):
    name = NameField(required=True, allow_none=False)
    surname = SurnameField(required=True, allow_none=False)
    age = AgeField(required=True, allow_none=False)
    email = EmailField(required=True, allow_none=False)
    password = PasswordField(required=True, allow_none=False)
    patronymic = PatronymicField(allow_none=False)
    phone = PhoneField(allow_none=False)

    @post_load
    def to_dto(self, data: tp.Dict[str, tp.Any], **kwargs: tp.Any):
        return UserRegisterDTO(**data)


class UserLoginSchema(Schema):
    email = EmailField(required=True, allow_none=False)
    password = PasswordField(required=True, allow_none=False)

    @post_load
    def to_dto(self, data: tp.Dict[str, tp.Any], **kwargs: tp.Any):
        return UserLoginDTO(**data)


# @dataclass(frozen=True)
# class UserLoginDTO:
#     email: str
#     password: str
#     confirm_password: str

#     @classmethod
#     def to_dto(
#         cls,
#         email: str,
#         password: str,
#         confirm_password: str,
#     ) -> UserLoginDTO:
#         return cls(email, password, confirm_password)


# @dataclass(frozen=True)
# class UserLogoutDTO:
#     id: int
#     token: str

#     @classmethod
#     def to_dto(cls, id: int, token: str) -> UserLogoutDTO:
#         return cls(id, token)
