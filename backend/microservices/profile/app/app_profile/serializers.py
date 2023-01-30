import typing as tp

from rest_framework import serializers
from rest_framework.serializers import Serializer

from app_profile import models


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        exclude = ("rating",)


class SwapHistorySerializer(serializers.Serializer):
    def to_representation(self, obj):
        return {
            "id": obj[0],
            "date": obj[1],
            "description": obj[2],
            "user": {
                "username": obj[3],
                "surname": obj[4],
                "patronymic": obj[5],
            },
        }


class SerializerFactory:
    __name: str

    __serializer_classes: tp.Dict[str, tp.Type[Serializer]] = {
        "swap_history": SwapHistorySerializer,
        "user": UserProfileSerializer,
    }

    def __init__(self, name: str) -> None:
        self.__name = name

    def create(self):
        serializer_class = self.__serializer_classes.get(self.__name)
        if serializer_class is not None:
            return serializer_class

        raise