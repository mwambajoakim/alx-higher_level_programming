#!/usr/bin/python3
"""
Prints all City objects from the database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_city import City
from model_state import Base, State


if __name__ == "__main__":
    user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]

    db_url = f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}"

    engine = create_engine(db_url, pool_pre_ping=True)

    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City, State).filter(
        State.id == City.state_id
    ).order_by(City.id).all()

    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
