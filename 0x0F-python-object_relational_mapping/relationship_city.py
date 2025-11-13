#!/usr/bin/python3
"""
Contains the class definition of a City
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """Creates a table for cities

       Attributes:
          id: The city id.
          name: The city name.
          state_id: Foreign key pointing to state of city.
          state: Child relationship to State.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities")
