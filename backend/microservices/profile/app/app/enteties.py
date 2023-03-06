from __future__ import annotations

import typing as tp
from abc import ABC
from datetime import datetime


class IUser(ABC):
    id: int
    username: str
    surname: str
    email: str
    patronymic: str
    age: int
    phone: str
    rating: float
    is_staf: bool
    is_active: bool

    swap_history: ISwapHistory
    swaps: tp.Iterable


class ISwapHistory(ABC):
    id: int
    user: IUser
    swaps: tp.Iterable[ISwap]


class ISwap(ABC):
    id: int
    user: IUser
    description: str
    assessment: int
    is_active: bool
    is_end: bool
    date: datetime
