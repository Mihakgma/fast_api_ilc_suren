from fastapi import Path, APIRouter
from typing import Annotated

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/{item_id}")
async def get_item_by_id(item_id: Annotated[int, Path(ge=0, le=1_000_000)]):
    return {"item_id": item_id}
