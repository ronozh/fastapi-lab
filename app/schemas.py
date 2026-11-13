from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str | None = None
    price: float = Field(gt=0)
    in_stock: bool = True


class ItemCreate(ItemBase):
    """Request body for creating an item."""


class ItemUpdate(BaseModel):
    """Request body for partial updates — every field is optional."""

    name: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = None
    price: float | None = Field(default=None, gt=0)
    in_stock: bool | None = None


class Item(ItemBase):
    """Response model — what the API returns."""

    id: int
