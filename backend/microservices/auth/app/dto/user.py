import typing as tp
from dataclasses import dataclass

from dto.token import TokenPairDTO


class UserDTO(tp.TypedDict):
    id: int
    name: str
    email: str
    phone: tp.Optional[str]


@dataclass(frozen=True)
class RegisterUserDTO:
    name: str
    email: str
    password: str
    phone: tp.Optional[str]


@dataclass(frozen=True)
class ResponseUserDTO:
    user: UserDTO
    tokens: TokenPairDTO


@dataclass(frozen=True)
class LoginUserDTO:
    email: str
    password: str


@dataclass(frozen=True)
class LogoutUserDTO:
    id: int
    refresh_token: str
