import typing as tp

from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from app_profile.serializers import UserProfileSerializer
from app_profile.services.profile import ProfileService
from app_profile.services.swap import SwapService
from app_profile.utils.decorators.inject import Inject
from app_profile.mixins import SerializerMixin

from app.exceptions.api import ApiError


class ProfileViewSet(
    mixins.RetrieveModelMixin,
    SerializerMixin,
    viewsets.GenericViewSet,
):
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

    @Inject(ProfileService)
    @action(detail=True, methods=["get"])
    def rating(self, request: Request, pk: int, service: ProfileService):
        rating = service.calculate_rating(profile_id=pk)
        return Response(status=200, data={"raiting": rating})

    @Inject(ProfileService)
    def get_queryset(self, service: ProfileService):
        user_profiles = service.get_all()
        return user_profiles


class SwapViewSet(viewsets.ViewSet):
    @Inject(SwapService)
    @action(detail=True, methods=["post"])
    def assessment(self, request: Request, pk: int, service: SwapService):
        assessment = request.data.get("assessment", None)
        if (assessment is None) or (not isinstance(assessment, int)):
            raise ApiError.bad_request(
                message="Некорректное поле assessment!",
                details=["Поле assessment должно быть целым чилом!"],
            )

        service.set_assessment(swap_id=pk, assessment=assessment)

        return Response(status=201)

    @Inject(SwapService)
    @action(detail=True, methods=["patch"])
    def complete(self, request: Request, pk: int, service: SwapService):
        service.complete(swap_id=pk)

        return Response(status=200)
