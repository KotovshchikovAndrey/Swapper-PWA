import typing as tp
from abc import ABC, abstractmethod

from swap_app.repositories.swap import ISwapRepository, get_swap_repository
from app.enteties import IUser, ISwapHistory, ISwap
from swap_app.models import Swap, SwapHistory


class ISwapService(ABC):
    repository: ISwapRepository

    @abstractmethod
    def get_swap_history(self, user: IUser) -> tp.Iterable[ISwap]:
        raise NotImplementedError()

    @abstractmethod
    def get_swap_detail(self, id: int) -> ISwap:
        raise NotImplementedError()

    @abstractmethod
    def get_swappers(self, user: IUser) -> tp.Iterable[IUser]:
        raise NotImplementedError()


class SwapService(ISwapService):
    def __init__(self, repository: ISwapRepository = get_swap_repository()) -> None:
        self.repository = repository

    def get_swap_history(self, user: IUser) -> tp.Iterable[ISwap]:
        history = self.repository.get_history(user_id=user.id)

    def get_swap_detail(self, id: int) -> ISwap:
        return super().get_swap_detail(id)

    def get_swappers(self, user: IUser) -> tp.Iterable[IUser]:
        return super().get_swappers(user)


######
swap_service = SwapService()


def get_swap_service(use_cache: bool = True) -> ISwapService:
    if use_cache:
        return swap_service

    return SwapService()
