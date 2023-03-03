import typing as tp
from dataclasses import dataclass

from core.entities import IUser


@dataclass(frozen=True)
class RegisterUserDTO:
    name: str
    email: str
    password: str
    phone: tp.Optional[str] = None


@dataclass(frozen=True)
class LoginUserDTO:
    email: str
    password: str


@dataclass(frozen=True)
class LogoutUserDTO:
    user: IUser
    token: str
