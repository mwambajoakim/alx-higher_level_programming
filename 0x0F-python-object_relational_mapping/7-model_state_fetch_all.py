#!/usr/bin/python3
"""
Lists all State objects from the database
"""
import MySQLdb
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user, passwd, db = sysargv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(f"mysql+mysqldb://{user):{passwd}@localhost:3306/{db}",
                           pool_pre_ping=True)

    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session=Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
