from sqlalchemy import Column, Float, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class FlightModel(Base):
    __tablename__ = 'flight'

    id = Column(Integer, primary_key=True)
    created = Column(Date)
    flightdate = Column(String(100))
    airlines = Column(String(255))
    travel = Column(Boolean)
    price = Column(Float(precision=2))
    departure = Column(String(100))
    arrival = Column(String(100))
