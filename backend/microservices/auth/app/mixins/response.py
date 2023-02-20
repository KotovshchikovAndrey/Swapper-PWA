# import typing as tp

from starlette.responses import JSONResponse

from core.entities import UserEntity
from dto.user import UserResponseDTO
from utils.mapper import ApiMapper


class UserResponseMixin:
    def get_user_response(
        self,
        user: UserEntity,
        access_token: str,
        refresh_token: str,
        status: int = 201,
    ):
        mapper = ApiMapper(dto=UserResponseDTO)
        dto = mapper.convert_to_dto(
            {
                "user": {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "phone": user.phone,
                },
                "tokens": {
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                },
            }
        )

        response = JSONResponse(
            status_code=status,
            content={"user": dto.user, "tokens": dto.tokens},
        )

        response.set_cookie(
            key="refresh_token",
            value=dto.tokens["refresh_token"],
            httponly=True,
            max_age=60 * 60 * 24 * 30,
        )

        return response
