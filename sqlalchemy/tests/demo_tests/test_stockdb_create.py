import unittest
from stockdb_declaration import User, Portfolio, Stock, StockHolding
from stockdb_create import add_user
from sautils import get_or_create
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://zhiqiang@localhost/stockdb', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


# TODO: Need to set up test database
class StockdbCreateTest(unittest.TestCase):

    def test_add_user(self):
        user = get_or_create(session, User, email='zach@test.com', password='Password1@')
        print(user)

        user = get_or_create(session, User, email='zach3@test.com', password='Password1@')
        print(user)

