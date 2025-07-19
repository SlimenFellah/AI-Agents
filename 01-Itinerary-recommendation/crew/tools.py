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