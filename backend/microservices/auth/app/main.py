from config import AppConfig

AppConfig.load_env_config()

from fastapi import FastAPI

from api.api_v1.routes import router as api_v1_router
from database import postgres
from errors.handler import errors_handler  # type: ignore

app = FastAPI()

app.middleware("http")(errors_handler)  # type: ignore
app.include_router(api_v1_router, prefix="/api/v1")


@app.on_event("startup")  # type: ignore
async def startup() -> None:
    await postgres.connect()


@app.on_event("shutdown")  # type: ignore
async def shutdown() -> None:
    await postgres.disconnect()
