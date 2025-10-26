from fastapi import FastAPI

import src
from src.api import api_router

app = FastAPI(
    title="My Dumb API",
    description="",
    swagger_ui_parameters={"displayRequestDuration": True},
    version=src.__version__,
)
app.include_router(api_router, prefix="/api")
