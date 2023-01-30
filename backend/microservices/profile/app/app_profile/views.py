import typing as tp

from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from app_profile.serializers import SerializerFactory, UserProfileSerializer
from app_profile.services.profile import ProfileService
from app_profile.services.swap import SwapService
from app_profile.utils.decorators.inject import Inject


class ProfileViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    serializer_class = UserProfileSerializer

    @Inject(ProfileService)
    @action(detail=True, methods=["get"])
    def user(self, request: Request, pk: int, service: ProfileService):
        user_representation = service.get_user_representation(user_id=pk)
        serializer = self.get_serializer(
            user_representation, serializer_name="representation"
        )

        return Response(status=200, data=serializer.data)

    @Inject(ProfileService)
    @action(url_path="swap.history", detail=False, methods=["get"])
    def swap_history(self, request: Request, service: ProfileService):
        swap_history = service.get_swap_history(profile_id=2)
        serializer = self.get_serializer(
            swap_history,
            many=True,
            serializer_name="swap_history",
        )

        return Response(status=200, data=serializer.data)

    # Вынести в отдельный ViewSet

    # @Inject(SwapService)
    # @action(detail=False, methods=["post"])
    # def assessment(self, request: Request, service: SwapService):
    #     swap_id = request.query_params.get("swap_id", None)
    #     if swap_id is None:
    #         raise

    #     assessment = request.data.get("assessment", None)
    #     if (assessment is None) or (not isinstance(assessment, int)):
    #         raise

    #     service.set_assessment(swap_id, assessment)

    #     return Response(status=201)

    @Inject(ProfileService)
    @action(detail=True, methods=["get"])
    def rating(self, request: Request, pk: int, service: ProfileService):
        rating = service.calculate_rating(profile_id=pk)

        return Response(status=200, data={"raiting": rating})

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
