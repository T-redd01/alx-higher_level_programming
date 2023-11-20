#!/usr/bin/python3
"""query db with orm"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import asc
import sys


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    states = session.query(State).order_by(asc(State.id))
    for state in states:
        if 'a' in state.name:
            print(f"{state.id}: {state.name}")
