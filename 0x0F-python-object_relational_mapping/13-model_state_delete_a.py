#!/usr/bin/python3
"""Start to link class to table in db
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select, insert

if __name__ == "__main__":
    code_base = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    _Session = sessionmaker(bind=code_base)
    this_session = _Session()
    delete_this_States = this_session.query(State).filter(State.name.like(f'%a%')).all()
    if delete_this_States:
        for state in delete_this_States:
            this_session.delete(state)
        this_session.commit()

    this_session.close()
