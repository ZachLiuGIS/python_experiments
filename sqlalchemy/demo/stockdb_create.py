import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from stockdb_declaration import User, Portfolio, Stock, StockHolding
from sautils import get_or_create
from pdutils import currency_column_to_number

echo = True
engine = create_engine('postgresql+psycopg2://zhiqiang@localhost/stockdb', echo=echo)
Session = sessionmaker(bind=engine)
session = Session()


def add_users():
    get_or_create(session, User, email='zach@test.com', password='Password1@')
    get_or_create(session, User, email='zach4@test.com', password='Password1@',
                  display_name='Zach4', first_name='ZachIV', last_name='Liu')
    user3 = get_or_create(session, User, email='zach3@test.com', password='Password1@')[0]
    user3.display_name = 'Zach3'


def add_stocks():
    with open('data/list.txt', 'r') as f:
        for symbol in f:
            get_or_create(session, Stock, symbol=symbol)


def add_stock_holdings():
    user = get_or_create(session, User, email='zach@test.com')[0]
    portfolio = get_or_create(session, Portfolio, user=user, name='My First Portfolio')[0]
    df = pd.read_csv('data/activity_until_20160222.csv', index_col=0, parse_dates=True, usecols=range(8))
    currency_column_to_number(df, 'Price')
    for row in df.iterrows():
        data = row[1]
        stock = get_or_create(session, Stock, symbol=data['Symbol'])[0]
        get_or_create(session, StockHolding,
                      shares=data['Quantity'], price=data['Price'], date=data['Date'],
                      portfolio=portfolio, stock=stock
                      )


def add_portfolios():
    user = get_or_create(session, User, email='zach@test.com')[0]
    get_or_create(session, Portfolio, user=user, name='My First Portfolio')
    get_or_create(session, Portfolio, user=user, name='My Second Portfolio')
    user2 = get_or_create(session, User, email='zach2@test.com')[0]
    get_or_create(session, Portfolio, user=user2, name='Zach2 First Portfolio')
    get_or_create(session, Portfolio, user=user2, name='Zach2 Second Portfolio')
    get_or_create(session, Portfolio, user=user2, name='Zach2 Third Portfolio')


def add_demo_data():
    add_users()
    add_portfolios()
    add_stocks()
    add_stock_holdings()


if __name__ == '__main__':
    add_demo_data()
    session.commit()
