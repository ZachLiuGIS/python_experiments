from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from stockdb_declaration import User, Portfolio, Stock, StockHolding

engine = create_engine('postgresql+psycopg2://zhiqiang@localhost/stockdb', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def add_users():
    user1 = User(email='zach@test.com', password='Password1@', display_name='Zach', first_name='Zach', last_name='Liu')
    user2 = User(email='zach2@test.com', password='Password1@', display_name='Zach II', first_name='ZachII', last_name='Liu')
    session.add(user1)
    session.add(user2)
    session.commit()


if __name__ == '__main__':
    add_users()
