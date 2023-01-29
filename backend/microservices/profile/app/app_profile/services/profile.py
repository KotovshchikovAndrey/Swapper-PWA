import typing as tp
from app_profile.services.user import UserService
from app_profile.services.swap import SwapService

from app_profile.models import SwapHistory, Swap


class ProfileService:
    __user_service: UserService
    __swap_service: SwapService

    def __init__(self, user_service: UserService, swap_service: SwapService) -> None:
        self.__user_service = user_service
        self.__swap_service = swap_service

    def get_swap_history(self, user_id: int) -> tp.Iterable[Swap]:
        user = self.__user_service.get_by_id(id=user_id)
        if user is None:
            raise

        swap_history = (
            SwapHistory.objects.prefetch_related("swaps")
            .only("swaps")
            .filter(user=user)
            .first()
        )

        if swap_history is not None:
            return swap_history.swaps.all()

        return []
