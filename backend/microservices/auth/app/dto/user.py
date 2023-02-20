import typing as tp
from dataclasses import dataclass

from dto.token import TokenPairDTO


class UserDTO(tp.TypedDict):
    id: int
    name: str
    email: str
    phone: tp.Optional[str]


@dataclass(frozen=True)
class UserResponseDTO:
    user: UserDTO
    tokens: TokenPairDTO


@dataclass(frozen=True)
class UserRegisterDTO:
    name: str
    email: str
    password: str


@dataclass(frozen=True)
class UserLoginDTO:
    email: str
    password: str


@dataclass(frozen=True)
class UserLogoutDTO:
    id: int
    refresh_token: str
