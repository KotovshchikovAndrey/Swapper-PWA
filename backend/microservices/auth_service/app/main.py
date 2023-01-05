import typing as tp

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from database.connections import *
from database.models import *
from errors.api_errors import ApiError

app = FastAPI()


@app.on_event("startup")
async def startup() -> None:
    await postgresql_connection.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    await postgresql_connection.disconnect()


@app.middleware("http")
async def error_handler(request: Request, call_next: tp.Callable):
    try:
        return await call_next(request)
    except Exception as exc:
        if isinstance(exc, ApiError):
            return JSONResponse(
                status_code=exc.status,
                content={"message": exc.message, "details": exc.details},
            )

        print(exc)
        return JSONResponse(
            status_code=500,
            content={"message": "Непредвиденная ошибка сервера", "details": []},
        )
