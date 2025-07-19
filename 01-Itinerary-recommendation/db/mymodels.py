from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    places = relationship("Place", back_populates="city")

class Place(Base):
    __tablename__ = "places"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    city_id = Column(Integer, ForeignKey("cities.id"))
    city = relationship("City", back_populates="places")
