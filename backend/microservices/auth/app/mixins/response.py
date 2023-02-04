import typing as tp

from starlette.responses import JSONResponse

from mappers.token import TokenMapper


class ResponseTokenPairMixin:
    def _get_response(self, tokens: tp.Tuple[str, str], status: int = 200):
        dto = TokenMapper.convert_to_token_pair_dto(tokens)
        response = JSONResponse(
            status_code=status,
            content={
                "access_token": dto.access_token,
                "refresh_token": dto.refresh_token,
            },
        )

        response.set_cookie(
            key="refresh_token",
            value=dto.refresh_token,
            httponly=True,
            max_age=60 * 60 * 24 * 30,
        )

        return response
