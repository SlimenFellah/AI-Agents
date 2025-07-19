from fastapi import FastAPI
from app.routes import cities, places

app = FastAPI(title="Algeria Tourism API")

app.include_router(cities.router)
app.include_router(places.router)
