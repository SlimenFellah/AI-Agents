from pydantic import BaseModel
from typing import List

class CitySchema(BaseModel):
    id: str
    name: str
    region: str
    description: str
    image_url: str

    class Config:
        orm_mode = True

class PlaceSchema(BaseModel):
    id: str
    city_id: str
    name: str
    category: str
    description: str
    opening_hours: str
    ticket_price: str
    latitude: float
    longitude: float
    image_url: str

    class Config:
        orm_mode = True
