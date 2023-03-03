# import typing as tp

from starlette.responses import JSONResponse


class TokenResponseMixin:
    def get_response(
        self,
        access_token: str,
        refresh_token: str,
        status: int = 200,
    ):
        response = JSONResponse(
            status_code=status,
            content={
                "access_token": access_token,
                "refresh_token": refresh_token,
            },
        )

        response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,
            max_age=60 * 60 * 24 * 30,
        )

        return response
