from datetime import datetime

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey


Base = declarative_base()


class Perform(Base):
    __tablename__ = 'perform'

    id              =   Column(Integer, primary_key=True)
    house           =   Column(String(100))
    hall            =   Column(String(100))
    name            =   Column(String(100))
    start_date      =   Column(DateTime)
    end_date        =   Column(DateTime)
    price_info      =   Column(Text)
    link            =   Column(Text)
    created_at      =   Column(DateTime)

    def __init__(self, house, hall, name, start_date, end_date, price_info, link):
        self.house              = house
        self.hall               = hall
        self.name               = name
        self.start_date         = start_date
        self.end_date           = end_date
        self.price_info         = price_info
        self.link               = link
        created_at              = datetime.now()











