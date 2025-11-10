#!/usr/bin/python3
"""
prints the State object with the name
passed as argument from the database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys


if __name__ == "__main__":
    user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    state_search = sys.argv[4]

    db_url = f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}"
    engine = create_engine(db_url, pool_pre_ping=True)

    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == state_search)).first()

    if states:
        print(states.id)
    else:
        print("Not found")

    session.close()
