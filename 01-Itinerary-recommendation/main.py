from fastapi import FastAPI
from api.routes import router
from db.seed import seed_data

app = FastAPI()

@app.on_event("startup")
def startup():
    seed_data()

app.include_router(router)

# uvicorn main:app --reload
