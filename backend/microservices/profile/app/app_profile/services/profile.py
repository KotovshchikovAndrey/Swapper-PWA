import typing as tp

from django.db import connection

from app_profile.models import UserProfile
from app.exceptions.api import ApiError


class ProfileService:
    __model: tp.Type[UserProfile]

    def __init__(self) -> None:
        self.__model = UserProfile

    def get_all(self):
        return self.__model.objects.all()

    def get_by_id(self, profile_id: int, fields: tp.Tuple[str] = ()) -> UserProfile:
        user_profile = self.__model.objects.only(*fields).filter(id=profile_id).first()
        if user_profile is None:
            raise ApiError.not_found(message="Профиль не найден!")

        return user_profile

    def get_user_representation(self, user_id: int) -> UserProfile:
        user_profile = self.get_by_id(
            profile_id=user_id,
            fields=("username", "surname", "patronymic", "age", "rating"),
        )

        return user_profile

    def get_swap_history(self, profile_id: int) -> tp.List[tp.Tuple]:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT app_profile_swap.id, date, description, username, surname, patronymic FROM app_profile_swap 
                JOIN app_profile_userprofile as profile_table ON profile_table.id = user_profile_id 
                WHERE app_profile_swap.id IN (
                    SELECT swap_id FROM app_profile_swaphistory_swaps WHERE swaphistory_id = (
                        SELECT id FROM app_profile_swaphistory WHERE user_profile_id=%s
                    )
                ) ORDER BY app_profile_swap.id
            """,
                (profile_id,),
            )
            swap_history = cursor.fetchall()

            return swap_history

    def update_rating(self, profile_id: int) -> None:
        user_profile = self.get_by_id(profile_id, fields=("rating",))
        user_profile.rating = self.calculate_rating(profile_id)
        user_profile.save(update_fields=("rating",))

    def calculate_rating(self, profile_id: int) -> tp.Optional[float]:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT ROUND(CAST (SUM(swap_table.assessment) AS NUMERIC) / COUNT(swap_id), 2)
                FROM app_profile_swaphistory_swaps as swap_hist_table 
                JOIN app_profile_swap as swap_table ON swap_table.id=swap_id
                WHERE swaphistory_id = (
                    SELECT swaphistory_id FROM app_profile_swaphistory as swap_hist_table 
                    WHERE user_profile_id = (
                        SELECT id FROM app_profile_userprofile WHERE id=%s
                    )
                )
            """,
                (profile_id,),
            )
            rating = cursor.fetchone()[0]

            return rating
