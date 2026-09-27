"""web-python-fastapi — FastAPI application factory."""

__version__ = "0.1.0"

from fastapi import FastAPI

from app.api.health import health_router
from app.api.v1 import api_router as v1_router
from app.core.errors import install_error_handlers

API_V1_PREFIX = "/api/v1"


def create_app() -> FastAPI:
    """Create the FastAPI application."""
    new_app = FastAPI(
        title="web-python-fastapi",
        description="",
        version=__version__,
    )

    install_error_handlers(new_app)
    new_app.include_router(health_router)
    new_app.include_router(v1_router, prefix=API_V1_PREFIX)

    return new_app


app = create_app()
