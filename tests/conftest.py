import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.routers.items import reset_db


@pytest.fixture
def client() -> TestClient:
    reset_db()
    return TestClient(app)
