from fastapi import HTTPException, status
from repositories import profile_repository

def list_profiles(db):
    return profile_repository.list_profiles(db)

def get_profile(db, profile_id: int):
    profile = profile_repository.get_profile(db, profile_id)
    if not profile:
        # Biznis logika: profil ne postoji
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found")
    return profile

def create_profile(db, profile):
    return profile_repository.create_profile(db, profile)

def update_profile(db, profile_id: int, profile):
    existing_profile = profile_repository.get_profile(db, profile_id)
    if not existing_profile:
        # Biznis logika: ne možemo updateovati nepostojeći profil
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found")
    return profile_repository.update_profile(db, profile_id, profile)

def delete_profile(db, profile_id: int):
    existing_profile = profile_repository.get_profile(db, profile_id)
    if not existing_profile:
        # Biznis logika: ne možemo obrisati nepostojeći profil
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found")
    profile_repository.delete_profile(db, profile_id)
    return {"message": "Profile deleted"}