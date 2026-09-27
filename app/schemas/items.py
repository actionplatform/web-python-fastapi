from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str


class Item(BaseModel):
    id: int
    name: str
