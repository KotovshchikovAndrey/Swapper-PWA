import typing as tp

from core.entities import IUser
from dataclasses import dataclass


class TokenPairDTO(tp.TypedDict):
    access_token: str
    refresh_token: str


@dataclass(frozen=True)
class RefreshTokenDTO:
    user: IUser
    access_token: str
    refresh_token: str
