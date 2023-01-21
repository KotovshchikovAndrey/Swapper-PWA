import typing as tp

from fastapi import APIRouter, Depends, Request

from api.dependencies.middlewares import UserMiddleware
from dto.user_dto import UserRegisterDTO

router = APIRouter(prefix="/auth")


@router.post(
    "/registration",
    name="registration",
    dependencies=[Depends(UserMiddleware.validate_registration_request)],
)
async def registration(user: UserRegisterDTO):
    return user


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
