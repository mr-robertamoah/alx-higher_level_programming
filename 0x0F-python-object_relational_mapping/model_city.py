#!/usr/bin/python3

"""
Contains the class definition of a City and
an instance Base = declarative_base()
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class City(Base):
    """class to map to cities table"""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, unique=True, nullable=True)
    name = Column(String(128), nullable=True)
    state_id = Column(Integer, nullable=True, ForeignKey("states.id"))
