from datetime import datetime

from sqlaalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


Base = declarative_base()


class Hall(Base):
    __tablename__ = 'hall'

    id          = Column(Integer, primary_key=True)
    house       = Column(String(100))
    name        = Column(String(100))
    created_at  = Column(DateTime)

    def __init__(self, house, name):
        self.house       = house
        self.name        = name
        created_at       = datetime.now()


class Concert(Base):
    __tablename__ = 'concert'

    id          = Column(Integer, primary_key=True)
    name        = Column(String(100))
    hall_id     = Column(Integer, ForeignKey('hall.id'))
    start_date  = Column(DateTime)
    end_date    = Column(DateTime)
    price       = Column(Integer)
    link        = Column(Text)
    created_at  = Column(DateTime)

    hall = relationship('hall')

    def __init__(self, hall_id, name, start_date, end_date, price, link):
        self.hall_id        = hall_id
        self.name           = name
        self.start_date     = start_date
        self.end_date       = end_date
        self.price          = price
        self.link           = link
        created_at          = datetime.now()











