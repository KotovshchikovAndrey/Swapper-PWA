import typing as tp

from app_profile.serializers import SerializerFactory


class SerializerMixin:
    def get_serializer(self, *args, serializer_name: tp.Optional[str] = None, **kwargs):
        if serializer_name is None:
            return super().get_serializer(*args, **kwargs)

        serializer_factory = SerializerFactory(name=serializer_name)
        serializer = serializer_factory.create()

        return serializer(*args, **kwargs)
