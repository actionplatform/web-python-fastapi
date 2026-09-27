import pytest

from app.core.errors import NotFoundError, ValidationError
from app.repositories.items import ItemRepository
from app.services.items import ItemService


def test_create_and_get_without_http():
    service = ItemService(ItemRepository())

    item = service.create(" pen ")

    assert item.name == "pen"
    assert service.get(item.id) == item
    assert service.list() == [item]


def test_refuses_bad_names_and_unknown_ids():
    service = ItemService(ItemRepository())

    with pytest.raises(ValidationError):
        service.create("")

    with pytest.raises(ValidationError):
        service.create("x" * 41)

    with pytest.raises(NotFoundError):
        service.get(1)
