# from crewai_tools import tool
# import requests

# @tool("GetCities")
# def get_cities():
#     """Fetch a list of cities from the tourism API"""
#     res = requests.get("http://localhost:8000/cities")
#     return res.json()

# @tool("GetPlacesByCity")
# def get_places_by_city(city_id: str):
#     """Fetch a list of places in a city by its ID"""
#     res = requests.get(f"http://localhost:8000/cities/{city_id}/places")
#     return res.json()


# import requests

# def get_cities():
#     """Fetch a list of cities from the tourism API"""
#     res = requests.get("http://localhost:8000/cities")
#     return res.json()

# def get_places_by_city(city_id: str):
#     """Fetch a list of places in a city by its ID"""
#     res = requests.get(f"http://localhost:8000/cities/{city_id}/places")
#     return res.json()

# from crewai import CrewTool
# import requests

# get_cities = CrewTool(
#     name="Get Cities",
#     description="Fetch a list of cities available in Algeria for tourism.",
#     func=lambda: requests.get("http://localhost:8000/cities").json()
# )

# get_places_by_city = CrewTool(
#     name="Get Places by City",
#     description="Fetch a list of places by city ID from the tourism API.",
#     func=lambda city_id: requests.get(f"http://localhost:8000/cities/{city_id}/places").json()
# )

# from langchain.tools import tool
# import requests

# @tool
# def get_cities() -> list:
#     """Fetch a list of cities available in Algeria for tourism."""
#     res = requests.get("http://localhost:8000/cities")
#     return res.json()

# @tool
# def get_places_by_city(city_id: str) -> list:
#     """Fetch a list of places to visit in a city by its ID."""
#     res = requests.get(f"http://localhost:8000/cities/{city_id}/places")
#     return res.json()

from crewai.tools import tool

@tool("Get Cities")
def get_cities() -> str:
    """Returns a list of cities in Algeria for itinerary planning."""
    return "Algiers, Oran, Constantine, Tlemcen, Ghardaia"

@tool("Get Places by City")
def get_places_by_city(city: str) -> str:
    """Returns popular places in a given Algerian city."""
    places = {
        "Algiers": ["Casbah", "Notre Dame d'Afrique", "Martyrs' Memorial"],
        "Oran": ["Santa Cruz Fort", "Place du 1er Novembre", "Aïn El-Turck beach"],
        "Constantine": ["Emir Abdelkader Mosque", "Suspension Bridge", "Palace of Ahmed Bey"]
    }
    return ", ".join(places.get(city, ["No known places for this city."]))