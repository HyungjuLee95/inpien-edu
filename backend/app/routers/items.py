from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..db import get_db
from ..deps import get_current_user
from ..models import Item, User
from ..schemas import ItemCreate, ItemResponse

router = APIRouter(prefix="/items", tags=["items"])


@router.get("", response_model=list[ItemResponse])
def list_items(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return list(db.scalars(select(Item).where(Item.user_id == current_user.id).order_by(Item.id.desc())).all())


@router.post("", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    item = Item(user_id=current_user.id, **payload.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
