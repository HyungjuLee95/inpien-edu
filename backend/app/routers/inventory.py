from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..db import get_db
from ..deps import get_current_user
from ..models import InventoryBatch, Item, Location, User
from ..schemas import InventoryBatchCreate, InventoryBatchResponse

router = APIRouter(prefix="/inventory/batches", tags=["inventory"])


@router.get("", response_model=list[InventoryBatchResponse])
def list_batches(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return list(
        db.scalars(
            select(InventoryBatch).where(InventoryBatch.user_id == current_user.id).order_by(InventoryBatch.id.desc())
        ).all()
    )


@router.post("", response_model=InventoryBatchResponse, status_code=status.HTTP_201_CREATED)
def create_batch(
    payload: InventoryBatchCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    item = db.scalar(select(Item).where(Item.id == payload.item_id, Item.user_id == current_user.id))
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    if payload.location_id is not None:
        location = db.scalar(
            select(Location).where(Location.id == payload.location_id, Location.user_id == current_user.id)
        )
        if not location:
            raise HTTPException(status_code=404, detail="Location not found")

    batch = InventoryBatch(user_id=current_user.id, **payload.model_dump())
    db.add(batch)
    db.commit()
    db.refresh(batch)
    return batch
