from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI

from api.api_v1.routes import router as api_v1_router
from database import postgres
from errors.handler import errors_handler

app = FastAPI()

app.middleware("http")(errors_handler)
app.include_router(api_v1_router, prefix="/api/v1")


@app.on_event("startup")
async def startup() -> None:
    await postgres.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    await postgres.disconnect()
