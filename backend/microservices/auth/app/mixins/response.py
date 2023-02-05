import typing as tp

from starlette.responses import JSONResponse

from dto.token import TokenPairDTO
from utils.mapper import ApiMapper


class ResponseTokenPairMixin:
    def _get_response(self, tokens: tp.Tuple[str, str], status: int = 200):
        access_token, refresh_token = tokens
        mapper = ApiMapper(dto=TokenPairDTO)
        dto = mapper.convert_to_dto(
            {"access_token": access_token, "refresh_token": refresh_token}
        )

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
