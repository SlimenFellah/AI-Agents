from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import City
from app.schemas import CitySchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/cities", response_model=list[CitySchema])
def list_cities(db: Session = Depends(get_db)):
    return db.query(City).all()
