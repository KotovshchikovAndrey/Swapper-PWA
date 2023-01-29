import typing as tp

from rest_framework import serializers
from rest_framework.serializers import Serializer

from app_profile import models


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        exclude = ("rating",)


class SwapSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Swap
        fields = "__all__"

    def to_representation(self, instance: models.Swap):
        user_full_name = self.__get_user_full_name(user_profile=instance.user_profile)

        return {
            "user": user_full_name,
            "description": instance.description,
            "date": instance.date,
        }

    def __get_user_full_name(self, user_profile: models.UserProfile) -> str:
        username, surname, patronymic = (
            user_profile.username,
            user_profile.surname,
            user_profile.patronymic,
        )

        full_name = f"{username} {surname}"
        if patronymic is not None:
            return full_name + f" {patronymic}"

        return full_name


class SerializerFactory:
    __name: str

    __serializer_classes: tp.Dict[str, tp.Type[Serializer]] = {
        "swap": SwapSerializer,
        "user": UserProfileSerializer,
    }

    def __init__(self, name: str) -> None:
        self.__name = name

    def create(self):
        serializer_class = self.__serializer_classes.get(self.__name)
        if serializer_class is not None:
            return serializer_class

        raise
