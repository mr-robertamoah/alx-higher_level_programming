#!/usr/bin/python3

"""
Contains the class definition of a State and
an instance Base = declarative_base()
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """class to map to states table"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, unique=True, nullable=True)
    name = Column(String(128), nullable=True)
