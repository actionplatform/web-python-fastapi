# web-python-fastapi



## Run

```bash
poetry install --with dev,code-quality
poetry run uvicorn app:app --reload    # http://localhost:8000/docs
```

## Test / lint

```bash
poetry run pytest
poetry run ruff check .
poetry run ruff format --check .
poetry run mypy --config-file .code_quality/mypy.ini .
```

## Layout

Five layers; each one depends only on the ones below it.

```
app/
├── __init__.py       create_app(), __version__
├── api/              HTTP only — routes, status codes, Depends; no rules
│   ├── health.py       GET /health
│   └── v1/           versioned routers; items is the example resource
├── schemas/          Pydantic — the contract of every request and response
├── services/         business rules; receive repositories, raise DomainError
├── repositories/     data access — one class per store, one method per query
└── core/             cross-cutting: errors
tests/
├── support/          builders shared by every test (make_client)
├── api/              contract through TestClient
└── services/         rules, with a repository and no HTTP
```

`api` calls `services`, never a repository. `services` raise `DomainError` subclasses (`NotFoundError`, `ValidationError`, `ConflictError`); `core/errors.py` turns them into `{"detail": {"code", "message", "field"}}`. `repositories` hold no rules and no HTTP — the in-memory one behind `items` is the placeholder for a database or an external API.
