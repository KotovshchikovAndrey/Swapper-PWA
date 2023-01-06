import typing as tp

from fastapi import APIRouter, Request

router = APIRouter(prefix="/auth")


@router.post("/registration")
async def registration(request: Request):
    pass


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
