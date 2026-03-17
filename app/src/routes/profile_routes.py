from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from misc.database import get_db
from services import profile_services
from schemas.profile_schemas import ProfileCreate, ProfileUpdate

profile_router = APIRouter(prefix="/api/v1/profiles")

@profile_router.get("/")
def list_profiles(db: Session = Depends(get_db)):
    return profile_services.list_profiles(db)

@profile_router.get("/{id}/")
def get_profile(id: int, db: Session = Depends(get_db)):
    return profile_services.get_profile(db, id)

@profile_router.post("/", status_code=status.HTTP_201_CREATED)
def create_profile(profile: ProfileCreate, db: Session = Depends(get_db)):
    return profile_services.create_profile(db, profile)

@profile_router.put("/{id}/", status_code=status.HTTP_200_OK)
def update_profile(id: int, profile: ProfileUpdate, db: Session = Depends(get_db)):
    return profile_services.update_profile(db, id, profile)

@profile_router.delete("/{id}/", status_code=status.HTTP_200_OK)
def delete_profile(id: int, db: Session = Depends(get_db)):
    return profile_services.delete_profile(db, id)