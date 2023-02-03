# import typing as tp
from dataclasses import dataclass


@dataclass(frozen=True)
class TokenPairDTO:
    access_token: str
    refresh_token: str


@dataclass(frozen=True)
class UpdateTokenDTO:
    user_id: int
    access_token: str
    refresh_token: str
