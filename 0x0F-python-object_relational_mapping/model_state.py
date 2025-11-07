#!/usr/bin/python3
"""
contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, create_engine


Base = declarative_base()

class State(Base):
    """Create a table called states.

      Attributes:
       id: id of the state.
       name: Name of the state.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

