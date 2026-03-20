from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class ProjectCreate(BaseModel):
    name: str
    profile_id: int
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    profile_id: Optional[int] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None