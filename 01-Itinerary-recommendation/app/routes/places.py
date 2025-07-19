from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Place
from app.schemas import PlaceSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/places", response_model=list[PlaceSchema])
def list_places(db: Session = Depends(get_db)):
    return db.query(Place).all()

@router.get("/cities/{city_id}/places", response_model=list[PlaceSchema])
def get_places_by_city(city_id: str, db: Session = Depends(get_db)):
    return db.query(Place).filter(Place.city_id == city_id).all()
