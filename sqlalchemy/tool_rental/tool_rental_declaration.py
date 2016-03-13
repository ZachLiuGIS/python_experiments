import os
import sys
import datetime
from sqlalchemy import create_engine, Table, Column
from sqlalchemy import (ForeignKey, Integer, String, Text, Numeric, Date, DateTime, Boolean)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

db_user = 'ZachLiu'
engine = create_engine('postgresql+psycopg2://' + db_user + '@localhost/tool_rental', echo=True)
Base = declarative_base()

reservation_tool = Table('reservation_tool', Base.metadata,
                         Column('reservation_number', ForeignKey('reservation.reservation_number'), primary_key=True),
                         Column('tool_number', ForeignKey('tool.tool_number'), primary_key=True)
                         )


class Customer(Base):
    __tablename__ = 'customer'

    email = Column(String(255), primary_key=True)
    first_name = Column(String(40))
    last_name = Column(String(40))
    password = Column(String(128), nullable=False)
    home_phone = Column(String(15))
    work_phone = Column(String(15))
    address1 = Column(String(35))
    address2 = Column(String(35))
    postal_code = Column(String(35))
    country = Column(String(35))

    def __repr__(self):
        return "<Customer: {}>".format(self.email)


class Clerk(Base):
    __tablename__ = 'clerk'

    username = Column(String(16), primary_key=True)
    first_name = Column(String(40))
    last_name = Column(String(40))
    password = Column(String(128), nullable=False)

    def __repr__(self):
        return "<Clerk: {}>".format(self.email)


class Reservation(Base):
    __tablename__ = 'reservation'

    reservation_number = Column(Integer, primary_key=True, autoincrement=True)
    start_date = Column(Date(), nullable=False)
    end_date = Column(Date(), nullable=False)
    card_number = Column(String(19), nullable=False)
    card_expiration_date = Column(Date(), nullable=False)

    customer_email = Column(String(255), ForeignKey('customer.email'))
    pickup_by = Column(String(16), ForeignKey('clerk.username'))
    dropoff_by = Column(String(16), ForeignKey('clerk.username'))

    customer = relationship("Customer", back_populates="reservations")
    pickup_clerk = relationship("Clerk", foreign_keys=[pickup_by], back_populates="reservation_pickups")
    dropoff_clerk = relationship("Clerk", foreign_keys=[dropoff_by], back_populates="reservation_dropoffs")

    # declare many to many without extra fields
    tools = relationship('Tool',
                         secondary=reservation_tool,
                         back_populates='reservations')

    def __repr__(self):
        return "<Reservation: {}>".format(self.reservation_number)


class Tool(Base):
    __tablename__ = 'tool'

    tool_number = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(15), nullable=False)
    short_description = Column(String(40), nullable=False)
    detailed_description = Column(Text())
    deposit_amount = Column(Numeric(6, 2), nullable=False)
    day_rental_price = Column(Numeric(6, 2), nullable=False)
    sell_date = Column(Date())
    status = Column(String(10), nullable=False)

    # declare many to many without extra fields
    reservations = relationship('Reservation',
                                secondary=reservation_tool,
                                back_populates='tools')

    def __repr__(self):
        return "<Tool: {}>".format(self.tool_number)


class Accessory(Base):
    __tablename__ = 'accessory'

    accessory = Column(String(50), nullable=False)
    tool_number = Column(Integer, ForeignKey('tool.tool_number'))

    tool = relationship("Tool", back_populates="accessories")

    def __repr__(self):
        return "<Accessory: {}>".format(self.accessory)


class ServiceRequest(Base):
    __tablename__ = 'service_order'

    tool_number = Column(Integer, ForeignKey('tool.tool_number'), primary_key=True)
    service_order_number = Column(Integer, primary_key=True)
    start_date = Column(Date(), nullable=False)
    end_date = Column(Date(), nullable=False)
    estimated_cost = Column(Numeric(6, 2), nullable=False)
    actual_cost = Column(Numeric(6, 2), nullable=False)

    tool = relationship("Tool", back_populates="service_orders")

    def __repr__(self):
        return "<ServiceRequest: {} - {}>".format(self.tool_number, self.service_order_number)
