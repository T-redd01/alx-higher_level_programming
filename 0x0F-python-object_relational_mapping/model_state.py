#!/usr/bin/python3
"""mapping class to table in sql"""
from sqlalchemy.ext.declarative import declative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """table being mapped to db

        Attributes:
            id: id of collumn
            name: state name in column
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
