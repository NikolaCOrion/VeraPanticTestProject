from typing import Optional
from pydantic import BaseModel


class ProfileCreate(BaseModel):
    name: str
    age: int


class ProfileUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
