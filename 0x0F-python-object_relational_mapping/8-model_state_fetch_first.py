#!/usr/bin/python3
"""
Prints the first State object from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}",
        pool_pre_ping=True)

    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).first()
    for state in states:
        print(f"{state.id}:{state.name}")
    print()

    session.close()
