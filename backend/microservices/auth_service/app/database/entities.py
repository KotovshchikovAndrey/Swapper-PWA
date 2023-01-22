import typing as tp


class UserEntity:
    id: int
    name: str
    surname: str
    age: int
    email: str
    password: str
    patronymic: tp.Optional[str] = None
    phone: tp.Optional[str] = None
    is_active: bool = False


class TokenEntity:
    id: int
    user: UserEntity
    value: str


class CodeEntity:
    id: int
    user: UserEntity
    value: int
