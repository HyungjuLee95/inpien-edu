from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    created_at: datetime


class ItemCreate(BaseModel):
    name: str
    category: str = "food"
    is_essential: bool = False
    default_shelf_life_days: int | None = None


class ItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    name: str
    category: str
    is_essential: bool
    default_shelf_life_days: int | None


class LocationCreate(BaseModel):
    name: str
    type: str = "room"


class LocationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    name: str
    type: str


class InventoryBatchCreate(BaseModel):
    item_id: int
    location_id: int | None = None
    quantity: int = 1
    unit: str = "ea"
    purchased_at: date | None = None
    expires_at: date | None = None


class InventoryBatchResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    item_id: int
    location_id: int | None
    quantity: int
    unit: str
    purchased_at: date | None
    expires_at: date | None
    status: str
