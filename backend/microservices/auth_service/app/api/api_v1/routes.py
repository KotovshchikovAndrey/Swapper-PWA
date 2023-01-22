import typing as tp

from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

from api.dependencies.middlewares import UserMiddleware
from database.connections import postgresql_connection
from database.repositories.user_repositories import UserPostgreSQLRepository
from domain.services import UserService
from dto.user_dto import UserRegisterDTO
from errors.api_errors import ApiError

router = APIRouter(prefix="/auth")


@router.post(
    "/registration",
    name="registration",
    dependencies=[Depends(UserMiddleware.validate_registration_request)],
)
@postgresql_connection.database.transaction()
async def registration(user: UserRegisterDTO):
    user_service = UserService(repository=UserPostgreSQLRepository())
    access_token, refresh_token = await user_service.register(user)

    response = JSONResponse(
        status_code=201,
        content={"access_token": access_token, "refresh_token": refresh_token},
    )
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        max_age=60 * 60 * 24 * 30,
    )

    return response


@router.post("/login")
async def login(request: Request):
    pass


@router.post("/refresh")
async def refresh(request: Request):
    pass


@router.delete("/logout")
async def logout(request: Request):
    pass


@router.get("/checkUserIsActive")
async def user_is_active(request: Request):
    pass


@router.post("/activateUserAccount")
async def activate_user_account(request: Request):
    pass
