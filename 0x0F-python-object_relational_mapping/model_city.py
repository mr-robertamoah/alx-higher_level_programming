#!/usr/bin/python3

"""
Contains the class definition of a City and
an instance Base = declarative_base()
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """class to map to cities table"""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, unique=True, nullable=True)
    name = Column(String(128), nullable=True)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=True)
