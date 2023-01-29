import typing as tp
from app_profile.models import User


class UserService:
    __model: tp.Type[User]

    def __init__(self) -> None:
        self.__model = User

    def get_by_id(self, id: int) -> tp.Optional[User]:
        return self.__model.objects.filter(id=id).first()
