#!/usr/bin/python3
"""
deletes all State objects with a name
containing the letter a from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]

    db_url = f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}"

    engine = create_engine(db_url, pool_pre_ping=True)

    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    a_states = session.query(State).filter(State.name.like("%a%")).all()

    for state in a_states:
        session.delete(state)
        session.commit()

    session.close()
