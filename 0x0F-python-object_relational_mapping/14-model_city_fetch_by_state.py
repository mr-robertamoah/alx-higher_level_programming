#!/usr/bin/python3

"""
This prints the first State object from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State, City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in (session.query(State.name, Cities.id, Cities.name)
                     .filter(State.id == City.state_id)):
        print("{} ({}) {}".format(instance[0], instance[1], instance[2]))
    session.commit()
