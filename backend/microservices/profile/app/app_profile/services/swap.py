import typing as tp
from app_profile.models import Swap


class SwapService:
    __model: tp.Type[Swap]

    def __init__(self) -> None:
        self.__model = Swap
