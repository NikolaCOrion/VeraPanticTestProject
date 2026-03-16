
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from misc.database import get_db

from services import profile_services


profile_router = APIRouter(prefix="/api/v1/profiles")


@profile_router.get("/")
def list_profiles(db=Depends(get_db)):
    return profile_services.list_profiles(db) 
