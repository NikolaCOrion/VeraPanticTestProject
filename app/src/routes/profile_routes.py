
from fastapi import APIRouter, Depends, status


from misc.database import get_db

from services import profile_services

from schemas.profile_schemas import ProfileCreate, ProfileUpdate


profile_router = APIRouter(prefix="/api/v1/profiles")


@profile_router.get("/")
def list_profiles(db=Depends(get_db)):
    return profile_services.list_profiles(db)


@profile_router.get("/{id}/")
def get_profile(id, db=Depends(get_db)):
    # implement GET ONE
    pass


@profile_router.post("/", status_code=status.HTTP_201_CREATED)
def create_profile(profile: ProfileCreate, db=Depends(get_db)):
    # implement POST
    pass


@profile_router.put("/{id}/", status_code=status.HTTP_200_OK)
def update_profile(id, profile: ProfileUpdate, db=Depends(get_db)):
    # implement PUT
    pass


@profile_router.delete("/{id}/", status_code=status.HTTP_200_OK)
def delete_profile(id, db=Depends(get_db)):
    # implement DELETE
    pass
