"""In-memory store standing in for a database or an external API. Replace it; keep the interface."""

from app.schemas.items import Item


class ItemRepository:
    def __init__(self) -> None:
        self.rows: dict[int, Item] = {}
        self.last_id = 0

    def list(self) -> list[Item]:
        return list(self.rows.values())

    def get(self, id: int) -> Item | None:
        return self.rows.get(id)

    def add(self, name: str) -> Item:
        self.last_id += 1
        item = Item(id=self.last_id, name=name)
        self.rows[item.id] = item

        return item


item_repository = ItemRepository()


def get_item_repository() -> ItemRepository:
    return item_repository
