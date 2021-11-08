from Model.FlightModel import FlightModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from Model.FlightModel import Base
from urllib.parse import quote
import config


def SessionLocal():
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{config.MYSQL_USER}:%s@{config.MYSQL_HOST}:{config.MYSQL_PORT}/{config.MYSQL_DATABASE}' % quote(
        f'{config.MYSQL_PASSWORD}')
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    if not engine.has_table(FlightModel.__tablename__):
        FlightModel.__table__.create(engine)
    Session = sessionmaker(bind=engine)

    return Session()
