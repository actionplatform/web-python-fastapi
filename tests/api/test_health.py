from app import __version__
from tests.support import make_client


def test_health():
    response = make_client().get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": __version__}
