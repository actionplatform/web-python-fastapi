"""Builders every test can share, so a change in setup is made once."""

from fastapi.testclient import TestClient

from app import create_app


def make_client() -> TestClient:
    return TestClient(create_app())
