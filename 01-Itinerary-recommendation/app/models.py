from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    __tablename__ = "cities"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    region = Column(String)
    description = Column(String)
    image_url = Column(String)

class Place(Base):
    __tablename__ = "places"
    id = Column(String, primary_key=True, index=True)
    city_id = Column(String, ForeignKey("cities.id"))
    name = Column(String)
    category = Column(String)
    description = Column(String)
    opening_hours = Column(String)
    ticket_price = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    image_url = Column(String)
