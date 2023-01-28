import typing as tp

from domain.mappers.base import BaseMapper
from dto import user


class UserMapper(BaseMapper):
    @classmethod
    def to_user_dto(cls, data: tp.Dict[str, tp.Any]) -> user.UserDTO:
        return cls.to_dto(user.UserDTO, data)

    @classmethod
    def to_response_dto(cls, data: tp.Dict[str, tp.Any]):
        pass
