import dataclasses
import typing as tp
from abc import ABC

T = tp.TypeVar("T", bound=object)


class BaseMapper(ABC):
    @staticmethod
    def to_dto(dto_cls: tp.Type[T], data: tp.Dict[str, tp.Any]) -> T:
        return dto_cls(**data)

    @staticmethod
    def get_fields(dto_cls: tp.Type[T]) -> tp.Tuple[str]:
        return tuple(field.name for field in dataclasses.fields(dto_cls))
