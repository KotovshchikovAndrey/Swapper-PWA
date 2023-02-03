import typing as tp

from dao.schemas.user import UserLoginSchema, UserRegisterSchema
from dto.user import UserLoginDTO, UserLogoutDTO, UserRegisterDTO


class UserMapper:
    @staticmethod
    def convert_to_register_dto(data: tp.Dict[str, tp.Any]) -> UserRegisterDTO:
        schema = UserRegisterSchema()
        dto = schema.load(data)  # type: ignore

        return dto  # type: ignore

    @staticmethod
    def convert_to_login_dto(data: tp.Dict[str, tp.Any]) -> UserLoginDTO:
        schema = UserLoginSchema()
        dto = schema.load(data)  # type: ignore

        return dto  # type: ignore

    @staticmethod
    def convert_to_logout_dto(id: int, token: str):
        return UserLogoutDTO(id, token)
