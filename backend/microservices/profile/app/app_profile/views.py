from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from rest_framework.decorators import action
from app_profile.services.profile import ProfileService
from app_profile.services.user import UserService
from app_profile.services.swap import SwapService

from app_profile.serializers import SwapSerializer


class ProfileView(viewsets.GenericViewSet):
    @action(detail=False, methods=["get"])
    def swap_history(self, request: Request):
        profile_service = ProfileService(
            user_service=UserService(), swap_service=SwapService()
        )

        swap_history = profile_service.get_swap_history(user_id=1)
        serializer = SwapSerializer(swap_history, many=True)

        return Response(status=200, data={"data": serializer.data})
