from tests.support import make_client


def test_create_list_and_get():
    client = make_client()

    created = client.post("/api/v1/items", json={"name": "pen"})

    assert created.status_code == 201
    assert created.json()["name"] == "pen"

    id = created.json()["id"]

    assert created.json() in client.get("/api/v1/items").json()
    assert client.get(f"/api/v1/items/{id}").json() == created.json()


def test_errors_have_one_shape():
    client = make_client()

    invalid = client.post("/api/v1/items", json={"name": "  "})
    missing = client.get("/api/v1/items/999999")

    assert invalid.status_code == 422
    assert invalid.json() == {
        "detail": {
            "code": "invalid",
            "message": "name is required",
            "field": "name",
        }
    }
    assert missing.status_code == 404
    assert missing.json()["detail"]["code"] == "not_found"
