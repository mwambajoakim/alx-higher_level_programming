#!/usr/bin/python3
"""
lists all State objects,
and corresponding City objects,
contained in the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    database_url = f"mysql+mysldb: "
    f"{username}:{password}@localhost:3306/{database}"

    engine = create_engine(database_url, pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).order_by(State.id).all()

    for state in results:
        _ = state.cities
        print(f"{state.id}: {state.name}")

    session.close()
