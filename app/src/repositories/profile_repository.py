import logging

from models.models import Profile as ProfileModel


def list_profiles(db):
    logging.info("Listing all profiles...")
    return db.query(ProfileModel).all()
