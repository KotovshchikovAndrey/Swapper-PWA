from fastapi import FastAPI

from api.api_v1.routes import router as api_v1_router
from database.connections import *
from database.models import *
from errors.handler import errors_handler

app = FastAPI()

app.middleware("http")(errors_handler)
app.include_router(api_v1_router, prefix="/api/v1")


@app.on_event("startup")
async def startup() -> None:
    await postgresql_connection.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    await postgresql_connection.disconnect()
