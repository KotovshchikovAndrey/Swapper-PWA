from rest_framework import serializers
from app_profile import models


class SwapSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Swap
        fields = "__all__"

    def to_representation(self, instance: models.Swap):
        user_full_name = self.__get_user_full_name(user_instance=instance.user)

        return {
            "user": user_full_name,
            "description": instance.description,
            "date": instance.date,
        }

    def __get_user_full_name(self, user_instance: models.User) -> str:
        name, surname, patronymic = (
            user_instance.name,
            user_instance.surname,
            user_instance.patronymic,
        )

        full_name = f"{name} {surname}"
        if patronymic is not None:
            return full_name + f" {patronymic}"

        return full_name
