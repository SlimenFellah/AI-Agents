from crewai import Task, Crew
from agents.city_planner import city_planner_agent
import logging


logging.basicConfig(level=logging.DEBUG)

city_task = Task(
    description="List the cities in Algeria and give 3 highlights from Oran",
    expected_output="A list of cities and top 3 destinations in Oran.",
    agent=city_planner_agent,
)

crew = Crew(
    agents=[city_planner_agent],
    tasks=[city_task],
    verbose=True
)

crew.kickoff()
