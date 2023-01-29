import typing as tp
from app_profile.models import Swap, SwapHistory


class SwapService:
    __model: tp.Type[Swap]

    def __init__(self) -> None:
        self.__model = Swap

    def get_history(self, user) -> tp.Iterable[Swap]:
        swap_history = (
            SwapHistory.objects.prefetch_related("swaps")
            .only("swaps")
            .filter(user=user)
            .first()
        )

        if swap_history is not None:
            return swap_history.swaps.all()

        return []
