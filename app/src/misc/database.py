import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists, drop_database

from models.models import Base

from misc.constants import DATABASE_URL, TESTING


if not TESTING:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
else:
    logging.info("TESTING MODE")
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    logging.info("DATABASE_URL: {}".format(DATABASE_URL))

    if database_exists(engine.url):
        logging.info("Dropping database before starting tests... ")
        drop_database(engine.url)

    if not database_exists(engine.url):
        create_database(engine.url)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
