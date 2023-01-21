import typing as tp

from domain.mappers.base_mapper import BaseMapper
from dto import user_dto


class UserMapper(BaseMapper):
    @classmethod
    def to_user_dto(cls, data: tp.Dict[str, tp.Any]) -> user_dto.UserDTO:
        return cls.to_dto(user_dto.UserDTO, data)

    @classmethod
    def to_response_dto(cls, data: tp.Dict[str, tp.Any]):
        pass
