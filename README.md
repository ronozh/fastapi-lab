# FastAPI Lab

A hands-on playground for learning [FastAPI](https://fastapi.tiangolo.com/).

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv sync                       # create .venv and install dependencies
uv run fastapi dev app/main.py  # start the dev server with auto-reload
```

Then open:

- http://127.0.0.1:8000 — the API
- http://127.0.0.1:8000/docs — interactive Swagger UI
- http://127.0.0.1:8000/redoc — ReDoc documentation

## Common commands

```bash
uv run pytest          # run tests
uv run ruff check .    # lint
uv run ruff format .   # format
uv add <package>       # add a dependency
```

## Project layout

```
app/
  main.py          # FastAPI app, root routes, router registration
  schemas.py       # Pydantic models (request/response shapes)
  routers/
    items.py       # CRUD example using an in-memory store
tests/             # pytest tests using FastAPI's TestClient
```

## Learning roadmap

- [x] Hello world, path & query parameters (`app/main.py`)
- [x] Pydantic request/response models & validation (`app/schemas.py`)
- [x] CRUD with `APIRouter`, status codes, `HTTPException` (`app/routers/items.py`)
- [x] Testing with `TestClient` (`tests/`)
- [ ] Dependency injection (`Depends`)
- [ ] Persist data with SQLite + SQLModel / SQLAlchemy
- [ ] Settings & environment variables (`pydantic-settings`)
- [ ] Authentication (OAuth2 + JWT)
- [ ] Async endpoints & background tasks
- [ ] Middleware, CORS, custom exception handlers
- [ ] File uploads & streaming responses
- [ ] WebSockets
- [ ] Docker & deployment
