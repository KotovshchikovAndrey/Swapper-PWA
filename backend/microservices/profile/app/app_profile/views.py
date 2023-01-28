from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response


class TestView(viewsets.GenericViewSet):
    def list(self, request: Request):
        return Response(status=200, data={"msg": "OK"})
