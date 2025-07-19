# from crewai import Task
# from agents.city_planner import city_planner_agent
# from tools import get_cities, get_places_by_city

# city_planner_agent.tools = [get_cities, get_places_by_city]

# recommendation_task = Task(
#     description="Suggest cities and places in Algeria to visit for a tourist interested in nature, history, and culture.",
#     expected_output="List of recommended cities and a daily itinerary with places to visit.",
#     agent=city_planner_agent
# )

from crewai import Task
from agents.city_planner import city_planner_agent

city_plan_task = Task(
    description=(
        "Suggest cities and places to visit in Algeria for a tourist "
        "interested in history, nature, and culture. The response should "
        "include a list of recommended cities and a proposed day-by-day itinerary "
        "with specific places to visit, drawn from the API."
    ),
    expected_output=(
        "A complete travel itinerary for a tourist, organized by day, "
        "with cities and places listed for each day, including descriptions."
    ),
    agent=city_planner_agent
)
