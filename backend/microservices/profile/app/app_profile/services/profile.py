import typing as tp

from django.db.models import Count, Sum
from django.db.models.query import QuerySet

from app_profile.models import Swap, UserProfile


class ProfileService:
    __model: tp.Type[UserProfile]

    def __init__(self) -> None:
        self.__model = UserProfile

    def get_all(self):
        return self.__model.objects.all()

    def get_by_id(self, profile_id: int) -> tp.Optional[UserProfile]:
        return self.__model.objects.filter(id=profile_id).first()

    def get_swap_history(self, profile_id: int) -> QuerySet[Swap]:
        user = (
            self.__model.objects.prefetch_related("swap_history__swaps")
            .only("swap_history__swaps")
            .filter(id=profile_id)
            .first()
        )
        if user is None:
            raise

        return user.swap_history.swaps

    def calculate_raiting(self, profile_id: int) -> float:
        swap_history = self.get_swap_history(profile_id)
        raiting = swap_history.aggregate(raiting=Sum("assessment") / Count("id"))[
            "raiting"
        ]

        return raiting
