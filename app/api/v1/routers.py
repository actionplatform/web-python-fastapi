"""Aggregate every v1 router here."""

from fastapi import APIRouter

from app.api.v1.items import items_router

v1 = APIRouter()
v1.include_router(items_router, prefix="/items", tags=["Items"])
