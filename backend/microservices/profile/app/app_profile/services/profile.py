import typing as tp

from django.db import connection
from django.db.models import Count, Sum

from app_profile.models import UserProfile


class ProfileService:
    __model: tp.Type[UserProfile]

    def __init__(self) -> None:
        self.__model = UserProfile

    def get_all(self):
        return self.__model.objects.all()

    def get_by_id(self, profile_id: int) -> tp.Optional[UserProfile]:
        return self.__model.objects.filter(id=profile_id).first()

    def get_swap_history(self, profile_id: int) -> tp.List[tp.Tuple]:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT app_profile_swap.id, date, description, username, surname, patronymic FROM app_profile_swap 
                JOIN app_profile_userprofile as profile_table ON profile_table.id = user_profile_id 
                WHERE app_profile_swap.id IN (
                    SELECT swap_id FROM app_profile_swaphistory_swaps WHERE swaphistory_id =
                    (
                        SELECT id FROM app_profile_swaphistory WHERE user_profile_id=%s
                    )
                )
            """,
                (profile_id,),
            )
            swap_history = cursor.fetchall()

            return swap_history

    def calculate_raiting(self, profile_id: int) -> tp.Optional[float]:
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
            raiting = cursor.fetchone()[0]

            return raiting
