from sqlalchemy.orm import Session

from misc.database import SessionLocal

from models.models import Profile as ProfileModel

from repositories.profile_repository import create_profile

from tests.conf import client



