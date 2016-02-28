import os
import sys
import datetime
from sqlalchemy import create_engine, Table, Column
from sqlalchemy import (ForeignKey, Integer, String, Text, Numeric, Date, DateTime, Boolean)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('postgresql+psycopg2://zhiqiang@localhost/stockdb', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    last_login = Column(DateTime(True), default=datetime.datetime.now)
    date_joined = Column(DateTime(True), default=datetime.datetime.now)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    display_name = Column(String(25), default='user')
    first_name = Column(String(40))
    last_name = Column(String(40))
    is_active = Column(Boolean(), default=True)

    portfolios = relationship("Portfolio", back_populates='user', cascade="all, delete-orphan")

    def __init__(self, email, password, display_name='user', first_name='', last_name=''):
        self.email = email
        self.password = password
        self.display_name = display_name
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "<User: {}>".format(self.email)


class Stock(Base):
    __tablename__ = 'stock'

    symbol = Column(String, primary_key=True)
    company_name = Column(String(128))
    sector = Column(String(128))

    portfolios = relationship("StockHolding", back_populates="stock", cascade="all, delete-orphan")

    def __repr__(self):
        return "<Stock: {}>".format(self.symbol)


class Portfolio(Base):
    __tablename__ = 'portfolio'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name = Column(String(50), nullable=False)
    description = Column(Text())

    user = relationship("User", back_populates="portfolios")

    stocks = relationship("StockHolding", back_populates="portfolio", cascade="all, delete-orphan")

    def __repr__(self):
        return "<Portfolio: {}>".format(self.name)


class StockHolding(Base):
    __tablename__ = 'stock_holding'

    id = Column(Integer, primary_key=True)
    stock_id = Column(String, ForeignKey('stock.symbol'))
    portfolio_id = Column(Integer, ForeignKey('portfolio.id'))
    shares = Column(Numeric(12, 3), nullable=False)
    price = Column(Numeric(10, 4), nullable=False)
    date = Column(Date(), nullable=False)
    created = Column(DateTime(True), default=datetime.datetime.now)
    modified = Column(DateTime(True), default=datetime.datetime.now, onupdate=datetime.datetime.now)

    stock = relationship("Stock", back_populates="portfolios")
    portfolio = relationship("Portfolio", back_populates="stocks")

    def __repr__(self):
        return "<StockHolding: {}>".format('')


if __name__ == '__main__':
    Base.metadata.create_all(engine)
