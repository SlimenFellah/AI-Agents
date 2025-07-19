from crewai import Agent
from tools import get_cities, get_places_by_city
from llm import llm

city_planner_agent = Agent(
    role="City Planner",
    goal="Plan amazing itineraries through Algeria",
    backstory="An expert in travel and culture who helps tourists explore Algeria",
    tools=[get_cities, get_places_by_city],
    llm=llm,
    verbose=True,
    allow_delegation=False
)
