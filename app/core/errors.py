"""Domain errors: services raise them, the app translates them to one JSON shape."""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class DomainError(Exception):
    status_code = 400
    code = "domain_error"

    def __init__(self, message: str, field: str | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.field = field

    def as_detail(self) -> dict:
        detail = {"code": self.code, "message": self.message}

        if self.field is not None:
            detail["field"] = self.field

        return detail


class NotFoundError(DomainError):
    status_code = 404
    code = "not_found"


class ValidationError(DomainError):
    status_code = 422
    code = "invalid"


class ConflictError(DomainError):
    status_code = 409
    code = "conflict"


def install_error_handlers(app: FastAPI) -> None:
    @app.exception_handler(DomainError)
    async def domain_error(_: Request, exc: DomainError) -> JSONResponse:
        return JSONResponse(
            status_code=exc.status_code, content={"detail": exc.as_detail()}
        )
