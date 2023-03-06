import typing as tp
from abc import ABC, abstractmethod

from app import settings
from profile_app.services.adapter import ApiAdapterFactory
from swap_app.services.swap import ISwapService, get_swap_service


class IProfileService(ABC):
    swap_service: any

    @abstractmethod
    def get_profile(self, email: str):
        adapter = ApiAdapterFactory.create(
            adapter_type="rest", host=settings.AUTH_SERVICE_API
        )


class ProfileService(IProfileService):
    def __init__(self, swap_service: ISwapService = get_swap_service()) -> None:
        self.swap_service = swap_service


#########
profile_service = ProfileService()


def get_profile_service(use_cache: bool = True) -> IProfileService:
    if use_cache:
        return profile_service

    return ProfileService()
