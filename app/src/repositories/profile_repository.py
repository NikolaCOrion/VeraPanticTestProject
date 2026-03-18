import logging

from models.models import Profile as ProfileModel


def list_profiles(db):
    logging.info("Listing all profiles...")
    return db.query(ProfileModel).all()

def get_profile(db, profile_id):
    return db.query(ProfileModel).filter(ProfileModel.id == profile_id).first()

def create_profile(db, profile):
    logging.info("Creating profile...")

    db_profile = ProfileModel(
        name=profile.name,
        age=profile.age,
    )

    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)  # osveži nakon commita

    return db_profile


def update_profile(db, profile_id, profile):
    db_profile = db.query(ProfileModel).filter(ProfileModel.id == profile_id).first()

    if not db_profile:
        return None

    update_data = profile.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_profile, key, value)

    db.commit()
    db.refresh(db_profile)

    return db_profile


def delete_profile(db, profile_id):
    logging.info(f"Deleting profile {profile_id}...")

    db_profile = db.query(ProfileModel).filter(ProfileModel.id == profile_id).first()

    if not db_profile:
        return None

    db.delete(db_profile)
    db.commit()

    return db_profile