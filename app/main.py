from fastapi import FastAPI

from app.routers import items

app = FastAPI(
    title="FastAPI Lab",
    description="A hands-on playground for learning FastAPI.",
    version="0.1.0",
)

app.include_router(items.router)


@app.get("/")
def root() -> dict[str, str]:
    """The simplest possible endpoint."""
    return {"message": "Hello, FastAPI!"}


@app.get("/hello/{name}")
def hello(name: str, excited: bool = False) -> dict[str, str]:
    """Path parameter (`name`) + optional query parameter (`?excited=true`)."""
    greeting = f"Hello, {name}"
    return {"message": greeting + ("!" if excited else ".")}
