from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Mount

# dependencies settings
from core import dependencies  # type: ignore

from api.api_v1.routes import routes as api_v1_routes
from api.middlewares.auth import JwtAuthBackend
from database.connections import postgres_db
from errors.handler import handle_error


async def startup() -> None:
    await postgres_db.connect()


async def shutdown() -> None:
    await postgres_db.disconnect()


routes = [Mount("/api/v1/auth", name="", routes=api_v1_routes)]
middlewares = [
    Middleware(
        CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
    ),
    Middleware(
        AuthenticationMiddleware,
        backend=JwtAuthBackend(),
    ),
]


app = Starlette(
    routes=routes,
    on_startup=[startup],
    on_shutdown=[shutdown],
    middleware=middlewares,
    exception_handlers={Exception: handle_error},
)
