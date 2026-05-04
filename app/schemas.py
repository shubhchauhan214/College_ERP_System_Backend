from datetime import date, datetime
from decimal import Decimal
from typing import Optional, List

from pydantic import BaseModel, ConfigDict


# ------------USER / AUTH ----------------
class UserCreate(BaseModel):
    full_name: str
    username: str
    passowrd: str
    role: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    full_name: str
    username: str
    role: str
    is_active: bool


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserOut

# ------------OWNER SESSION ----------------
class OwnerSessionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    owner_active: bool
    activated_by: Optional[int] = None
    activated_at: Optional[datetime] = None