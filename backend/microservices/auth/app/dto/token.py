import typing as tp
from dataclasses import dataclass

from core.entities import IUser


class TokenPairDTO(tp.TypedDict):
    access_token: str
    refresh_token: str


@dataclass(frozen=True)
class RefreshTokenDTO:
    user: IUser
    access_token: str
    refresh_token: str
