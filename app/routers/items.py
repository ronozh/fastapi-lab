"""A small CRUD example backed by an in-memory dict.

Later exercise: swap the dict for a real database (e.g. SQLite + SQLModel).
"""

from fastapi import APIRouter, HTTPException, status

from app.schemas import Item, ItemCreate, ItemUpdate

router = APIRouter(prefix="/items", tags=["items"])

_db: dict[int, Item] = {}
_next_id = 1


def _get_or_404(item_id: int) -> Item:
    item = _db.get(item_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item


@router.get("/", response_model=list[Item])
def list_items(skip: int = 0, limit: int = 10) -> list[Item]:
    return list(_db.values())[skip : skip + limit]


@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate) -> Item:
    global _next_id
    item = Item(id=_next_id, **payload.model_dump())
    _db[item.id] = item
    _next_id += 1
    return item


@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    return _get_or_404(item_id)


@router.patch("/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemUpdate) -> Item:
    item = _get_or_404(item_id)
    updated = item.model_copy(update=payload.model_dump(exclude_unset=True))
    _db[item_id] = updated
    return updated


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int) -> None:
    _get_or_404(item_id)
    del _db[item_id]


def reset_db() -> None:
    """Test helper: clear all items."""
    global _next_id
    _db.clear()
    _next_id = 1
