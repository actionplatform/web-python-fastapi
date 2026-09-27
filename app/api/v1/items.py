"""Example resource showing the layers: router → service → repository."""

from fastapi import APIRouter, Depends

from app.schemas.items import Item, ItemCreate
from app.services.items import ItemService

items_router = APIRouter()


@items_router.get("")
def list_items(service: ItemService = Depends(ItemService)) -> list[Item]:
    return service.list()


@items_router.post("", status_code=201)
def create_item(
    body: ItemCreate, service: ItemService = Depends(ItemService)
) -> Item:
    return service.create(body.name)


@items_router.get("/{id}")
def get_item(id: int, service: ItemService = Depends(ItemService)) -> Item:
    return service.get(id)
