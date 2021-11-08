from Model.Database import SessionLocal
from Model.FlightModel import FlightModel
import datetime


class FlightDTO:
    def __init__(self):
        self.db = SessionLocal()

    def saveFlight(self, **kwargs):
        new_flight = FlightModel(created=datetime.date.today(), flightdate=str(kwargs['month']),
                                 airlines=str(kwargs['airlines']), travel=False, price=float(kwargs['price']),
                                 departure=str(kwargs['origin']), arrival=str(kwargs['destination']))
        self.db.add(new_flight)
        self.db.commit()
