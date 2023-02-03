import typing as tp
from dataclasses import dataclass


@dataclass(frozen=True)
class UserRegisterDTO:
    name: str
    surname: str
    email: str
    age: int
    password: str
    patronymic: tp.Optional[str] = None
    phone: tp.Optional[str] = None


@dataclass(frozen=True)
class UserLoginDTO:
    email: str
    password: str


@dataclass(frozen=True)
class UserLogoutDTO:
    id: int
    refresh_token: str
