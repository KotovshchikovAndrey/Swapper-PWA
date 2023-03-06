import typing as tp
from abc import ABC, abstractmethod

from django.db.backends.utils import CursorWrapper
from django.db import connection
from app.enteties import IUser, ISwap
from swap_app.models import Swap


class ISwapRepository(ABC):
    database: CursorWrapper

    @abstractmethod
    def get_history(self, user_id: int):
        raise NotImplementedError()

    @abstractmethod
    def get_detail(self, id: int) -> ISwap:
        raise NotImplementedError()

    @abstractmethod
    def get_swappers(self, user: IUser):
        raise NotImplementedError()


class SwapPostgresRepository(ISwapRepository):
    def __init__(self) -> None:
        self.database = connection.cursor()

    def get_history(self, user_id: int):
        with self.database as db:
            db.execute(
                """
                    SELECT username, date FROM "swap_app_swap" JOIN "profile_app_user" ON user_id = profile_app_user.id
                    WHERE is_end = false and swap_app_swap.id in (
                        SELECT swap_id FROM "swap_app_swaphistory_swaps" 
                        WHERE swaphistory_id in ( SELECT id FROM "swap_app_swaphistory" 
                            WHERE user_id = %s
                        )
                    )
              """,
                (user_id,),
            )

            return db.fetchall()

    def get_detail(self, id: int):
        return Swap.objects.filter(id=id).first()

    def get_swappers(self, user_id: int):
        with self.database as db:
            db.execute(
                """
                    SELECT username, surname, email FROM "swap_app_swap" JOIN "profile_app_user" ON user_id = profile_app_user.id
                    WHERE is_end = false and swap_app_swap.id in (
                        SELECT swap_id FROM "swap_app_swaphistory_swaps" 
                        WHERE swaphistory_id in ( SELECT id FROM "swap_app_swaphistory" 
                            WHERE user_id = %s
                        )
                    ) 
                """,
                (user_id,),
            )

            return db.fetchall()


#########
swap_repository = SwapPostgresRepository()


def get_swap_repository(use_cache: True) -> ISwapRepository:
    if use_cache:
        return swap_repository

    return SwapPostgresRepository()
