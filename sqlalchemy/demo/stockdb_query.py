import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from stockdb_declaration import User, Portfolio, Stock, StockHolding

from sautils import get_or_create


echo = True
engine = create_engine('postgresql+psycopg2://zhiqiang@localhost/stockdb', echo=echo)
Session = sessionmaker(bind=engine)
session = Session()


def query_demo():
    user = get_or_create(session, User, email="zach@test.com")[0]
    portfolio = session.query(Portfolio).filter(Portfolio.name == 'My First Portfolio',
                                                Portfolio.user == user)
    print()
    print(portfolio[0])


query_demo()
