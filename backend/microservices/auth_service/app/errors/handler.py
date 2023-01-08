import typing as tp

from fastapi.requests import Request
from fastapi.responses import JSONResponse

from errors.api_errors import ApiError


async def errors_handler(request: Request, call_next: tp.Callable):
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
