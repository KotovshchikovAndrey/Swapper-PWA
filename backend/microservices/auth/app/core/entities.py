import typing as tp


class UserEntity:
    id: int
    name: str
    email: str
    password: str
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
