#!/usr/bin/python3
"""
changes the name of a State
object from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == "__main__":
    user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    db_url = f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}"

    engine = create_engine(db_url, pool_pre_ping=True)

    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    change_name = session.query(State).filter(State.id == 2).first()

    change_name.name = "New Mexico"

    session.commit()

    session.close()
