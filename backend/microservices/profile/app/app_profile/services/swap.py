import typing as tp

from app_profile.models import Swap


class SwapService:
    __model: tp.Type[Swap]

    def __init__(self) -> None:
        self.__model = Swap

    def set_assessment(self, swap_id: int, assessment: int) -> None:
        swap = self.__model.objects.filter(id=swap_id).first()
        if swap is None:
            raise

        if not swap.is_end:
            # оценить можно только после завершения сделки
            raise

        if not (0 <= assessment <= 5):
            # только от 0 до 5
            raise

        swap.assessment = assessment
        swap.save(update_fields=("assessment",))

        return
