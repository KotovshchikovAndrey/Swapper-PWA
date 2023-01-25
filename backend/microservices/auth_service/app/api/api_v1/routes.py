import typing as tp

from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

from api.dependencies.middlewares import UserMiddleware
from database.connections import postgresql_connection
from database.repositories.user import UserPostgreSQLRepository
from domain.services import UserService
from dto.user import UserLoginDTO, UserRegisterDTO

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
        content={
            "message": "Вы успешно зарегистрировались!",
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


@router.post(
    "/login",
    name="login",
    dependencies=[Depends(UserMiddleware.validate_login_request)],
)
@postgresql_connection.database.transaction()
async def login(user: UserLoginDTO):
    user_service = UserService(repository=UserPostgreSQLRepository())
    access_token, refresh_token = await user_service.login(user)

    response = JSONResponse(
        status_code=200,
        content={
            "message": "Вы успешно авторизовались!",
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


@router.post("/refresh", dependencies=[Depends(UserMiddleware.check_can_refresh)])
async def refresh(request: Request):
    user_service = UserService(repository=UserPostgreSQLRepository())
    new_access_token, new_refresh_token = await user_service.refresh_token_pair(
        payload=request.user_payload,
        old_refresh_token=request.cookies["refresh_token"],
    )

    response = JSONResponse(
        status_code=200,
        content={
            "message": "Токен обновлен!",
            "access_token": new_access_token,
            "refresh_token": new_refresh_token,
        },
    )
    response.set_cookie(
        key="refresh_token",
        value=new_refresh_token,
        httponly=True,
        max_age=60 * 60 * 24 * 30,
    )

    return response


@router.delete(
    "/logout",
    dependencies=[
        Depends(UserMiddleware.check_auth),
        Depends(UserMiddleware.check_can_refresh),
    ],
)
async def logout(request: Request):
    user_payload = request.user_payload
    user_service = UserService(repository=UserPostgreSQLRepository())
    await user_service.logout(
        user_id=user_payload["id"],
        token=request.cookies["refresh_token"],
    )

    response = JSONResponse(status_code=200, content={"message": "Вы разлогинены!"})
    response.delete_cookie("refresh_token")

    return response


@router.get("/checkUserIsActive")
async def user_is_active(request: Request):
    pass


@router.post("/activateUserAccount")
async def activate_user_account(request: Request):
    pass
