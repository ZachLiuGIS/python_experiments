from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from stockdb_declaration import User, Portfolio, Stock, StockHolding
from sautils import get_or_create

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



def add_user(email, password, display_name='', first_name='', last_name=''):
    try:
        user = session.query(User).filter(User.email == email, User.password == password).one()
    except NoResultFound:
        user = User(
                email=email, password=password,
                display_name=display_name, first_name=first_name, last_name=last_name
        )
        session.add(user)
    return user


def add_portfolios():
    user = get_or_create(session, User, email='zach@test.com')[0]
    get_or_create(session, Portfolio, user=user, name='My First Portfolio')
    get_or_create(session, Portfolio, user=user, name='My Second Portfolio')
    user2 = get_or_create(session, User, email='zach2@test.com')[0]
    get_or_create(session, Portfolio, user=user2, name='Zach2 First Portfolio')
    get_or_create(session, Portfolio, user=user2, name='Zach2 Second Portfolio')
    get_or_create(session, Portfolio, user=user2, name='Zach2 Third Portfolio')


def add_stock():
    pass


def add_stock_holding():
    pass


if __name__ == '__main__':
    add_users()
    add_portfolios()
    session.commit()
