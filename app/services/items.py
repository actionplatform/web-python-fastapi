from fastapi import Depends

from app.core.errors import NotFoundError, ValidationError
from app.repositories.items import ItemRepository, get_item_repository
from app.schemas.items import Item

MAX_NAME = 40


class ItemService:
    def __init__(
        self, repository: ItemRepository = Depends(get_item_repository)
    ) -> None:
        self.repository = repository

    def list(self) -> list[Item]:
        return self.repository.list()

    def get(self, id: int) -> Item:
        item = self.repository.get(id)

        if item is None:
            raise NotFoundError(f"item {id} not found")

        return item

    def create(self, name: str) -> Item:
        name = name.strip()

        if not name:
            raise ValidationError("name is required", field="name")

        if len(name) > MAX_NAME:
            raise ValidationError(
                f"name is longer than {MAX_NAME} characters", field="name"
            )

        return self.repository.add(name)
