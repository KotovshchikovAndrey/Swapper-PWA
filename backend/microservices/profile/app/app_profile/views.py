import typing as tp

from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from app_profile.serializers import SerializerFactory, UserProfileSerializer
from app_profile.services.profile import ProfileService


class ProfileViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    serializer_class = UserProfileSerializer

    @action(url_path="swap.history", detail=False, methods=["get"])
    def swap_history(self, request: Request):
        profile_service = ProfileService()
        swap_history = profile_service.get_swap_history(profile_id=2)
        serializer = self.get_serializer(
            swap_history,
            many=True,
            serializer_name="swap",
        )

        return Response(status=200, data=serializer.data)

    @action(detail=True, methods=["get"])
    def raiting(self, request: Request, pk: int):
        profile_service = ProfileService()
        raiting = profile_service.calculate_raiting(profile_id=pk)

        return Response(status=200, data={"raiting": raiting})

    def get_queryset(self):
        profile_service = ProfileService()
        user_profiles = profile_service.get_all()

        return user_profiles

    def get_serializer(self, *args, serializer_name: tp.Optional[str] = None, **kwargs):
        if serializer_name is None:
            return super().get_serializer(*args, **kwargs)

        serializer_factory = SerializerFactory(name=serializer_name)
        serializer = serializer_factory.create()

        return serializer(*args, **kwargs)
