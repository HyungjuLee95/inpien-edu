from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..db import get_db
from ..deps import get_current_user
from ..models import Location, User
from ..schemas import LocationCreate, LocationResponse

router = APIRouter(prefix="/locations", tags=["locations"])


@router.get("", response_model=list[LocationResponse])
def list_locations(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return list(
        db.scalars(select(Location).where(Location.user_id == current_user.id).order_by(Location.id.desc())).all()
    )


@router.post("", response_model=LocationResponse, status_code=status.HTTP_201_CREATED)
def create_location(
    payload: LocationCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    location = Location(user_id=current_user.id, **payload.model_dump())
    db.add(location)
    db.commit()
    db.refresh(location)
    return location
