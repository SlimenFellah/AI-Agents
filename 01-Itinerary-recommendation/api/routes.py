from fastapi import APIRouter
from mycrew.mycrew import build_crew

router = APIRouter()

@router.get("/generate-itinerary")
def generate_itinerary():
    crew = build_crew()
    result = crew.kickoff()
    return {"result": result}
