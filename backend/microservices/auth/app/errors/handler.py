import typing as tp

from fastapi.requests import Request
from fastapi.responses import JSONResponse

from errors.api import ApiError
from errors.config import ConfigError


async def errors_handler(request: Request, call_next: tp.Callable):  # type: ignore
    try:
        return await call_next(request)  # type: ignore
    except Exception as exc:
        if isinstance(exc, ApiError):
            return JSONResponse(
                status_code=exc.status,
                content={"message": exc.message, "details": exc.details},
            )

        if isinstance(exc, ConfigError):
            print(exc.message)
            return JSONResponse(
                status_code=500,
                content={"message": "Ошибка конфигурации сервера", "details": []},
            )

        print(exc)
        return JSONResponse(
            status_code=500,
            content={"message": "Непредвиденная ошибка сервера", "details": []},
        )
