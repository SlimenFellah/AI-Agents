# from crewai import Crew
# from agents.city_planner import city_planner_agent
# from tasks.city_plan_task import city_plan_task
# from tools import get_cities, get_places_by_city

# city_planner_agent.tools = [get_cities, get_places_by_city]

# crew = Crew(
#     agents=[city_planner_agent],
#     tasks=[city_plan_task],
#     verbose=True
# )

# if __name__ == "__main__":
#     result = crew.run()
#     print("\n✅ Final Itinerary Recommendation:")
#     print(result)

# from agents.city_planner import city_planner_agent
# from tasks.city_plan_task import city_plan_task
# from tools import get_cities, get_places_by_city
# from crewai import Crew

# # Assign tools to agent
# city_planner_agent.tools = [get_cities, get_places_by_city]

# crew = Crew(
#     agents=[city_planner_agent],
#     tasks=[city_plan_task],
#     verbose=True
# )

# if __name__ == "__main__":
#     result = crew.run()
#     print("\n✅ Final Recommendation:")
#     print(result)


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
