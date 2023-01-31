import typing as tp

from app.exceptions.api import ApiError
from app_profile.models import Swap


class SwapService:
    __model: tp.Type[Swap]

    def __init__(self) -> None:
        self.__model = Swap

    def set_assessment(self, swap_id: int, assessment: int) -> None:
        swap = self.get_by_id(swap_id)
        if not swap.is_end:
            raise ApiError.bad_request(
                message="Оценить свап можно только после окончания сделки!"
            )

        if not (0 <= assessment <= 5):
            raise ApiError.bad_request(message="Оценка должна быть числом от 0 до 5!")

        swap.assessment = assessment
        swap.save(update_fields=("assessment",))

    def complete(self, swap_id: int):
        swap = self.get_by_id(swap_id, fields=("is_end",))
        swap.is_end = True
        swap.save(update_fields=("is_end",))

    def get_by_id(self, swap_id: int, fields: tp.Tuple[str] = ()) -> Swap:
        swap = self.__model.objects.only(*fields).filter(id=swap_id).first()
        if swap is None:
            raise ApiError.bad_request("Свап не найден!")

        return swap
