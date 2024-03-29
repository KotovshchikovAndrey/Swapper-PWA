from starlette.requests import Request
from starlette.responses import JSONResponse

from errors.exceptions.api import ApiError

HEADERS = {"Access-Control-Allow-Origin": "*"}


async def handle_error(request: Request, exc: Exception):
    if isinstance(exc, ApiError):
        return JSONResponse(
            status_code=exc.status,
            content={"message": exc.message, "details": exc.details},
            headers=HEADERS,
        )

    print(exc)
    return JSONResponse(
        status_code=500,
        content={"message": "Непредвиденная ошибка сервера!", "details": {}},
        headers=HEADERS,
    )
