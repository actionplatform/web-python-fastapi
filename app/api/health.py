"""Health. Every API exposes it at the root."""

from fastapi import APIRouter

from app.schemas.health import Health

health_router = APIRouter(tags=["Health"])


@health_router.get("/health")
def health() -> Health:
    from app import __version__

    return Health(status="ok", version=__version__)
