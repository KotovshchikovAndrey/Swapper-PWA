import typing as tp
from dataclasses import dataclass


class TokenPairDTO(tp.TypedDict):
    access_token: str
    refresh_token: str


@dataclass(frozen=True)
class TokenUpdateDTO:
    user_id: int
    access_token: str
    refresh_token: str
