from db.mymodels import Base, City, Place
from db.database import engine, SessionLocal

def seed_data():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    if db.query(City).first(): return

    algiers = City(name="Algiers")
    oran = City(name="Oran")
    constantine = City(name="Constantine")

    db.add_all([algiers, oran, constantine])
    db.commit()

    db.add_all([
        Place(name="Casbah", description="Historic medina of Algiers", city=algiers),
        Place(name="Notre Dame d'Afrique", description="Famous basilica", city=algiers),
        Place(name="Fort Santa Cruz", description="Spanish fortress in Oran", city=oran),
        Place(name="Bey's Palace", description="Historic Ottoman palace", city=constantine),
    ])
    db.commit()
    db.close()
