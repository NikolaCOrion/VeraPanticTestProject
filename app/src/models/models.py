from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Float, nullable=False)
