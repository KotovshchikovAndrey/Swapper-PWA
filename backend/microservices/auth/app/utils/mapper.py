import typing as tp

from marshmallow import Schema, ValidationError

from errors.exceptions.api import ApiError

T = tp.TypeVar("T")


class ApiMapper(tp.Generic[T]):
    __dto: tp.Type[object]
    __schema: tp.Optional[Schema]

    def __init__(self, dto: tp.Type[T], schema: tp.Optional[Schema] = None) -> None:
        self.__dto = dto
        self.__schema = schema

    def convert_to_dto(self, data: tp.Mapping[str, tp.Any]) -> T:
        if self.__schema is None:
            return self.__dto(**data)  # type: ignore

        try:
            cleanes_data = self.__schema.load(data)  # type: ignore
            return self.__dto(**cleanes_data)  # type: ignore
        except ValidationError as exc:
            error_messages = self.__parse_error_messages(errors=exc.messages_dict)
            raise ApiError.bad_request(
                message="Получены невалидные данные!", details=error_messages
            )

    def __parse_error_messages(
        self, errors: tp.Dict[str, tp.List[str]]
    ) -> tp.List[str]:
        return [message for field in errors for message in errors[field]]
