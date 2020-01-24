from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey


db = SQLAlchemy()


class Perform(db.Model):
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











