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
