#!/usr/bin/python3
"""
Contains the class definition of a City
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import State, Base


class City(Base):
    """Creates a table for cities

       Attributes:
          id: The city id.
          name: The city name.
          state_id: Foreign key pointing to state of city.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
