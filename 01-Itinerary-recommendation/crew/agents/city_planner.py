# from crewai import Agent
# from llm import llm

# city_planner_agent = Agent(
#     role="City Planner",
#     goal="Help tourists plan personalized travel itineraries across Algeria",
#     backstory="You are an expert Algerian tour planner with deep knowledge of attractions and logistics.",
#     tools=[],  # Set in main runner
#     allow_delegation=False,
#     llm=llm
# )

# from crewai import Agent
# from llm import llm
# from tools import get_cities, get_places_by_city

# city_planner_agent = Agent(
#     role="City Planner",
#     goal="Help tourists explore Algeria with personalized and rich recommendations",
#     backstory="You're a travel expert for Algeria with deep knowledge of cities, places, and cultural heritage.",
#     tools=[get_cities, get_places_by_city],
#     allow_delegation=False,
#     llm=llm,
#     verbose=True
# )

# from crewai import Agent
# from llm import llm
# from tools import get_cities, get_places_by_city

# # Workaround to make tools compatible
# # tools = [get_cities.to_toolkit()[0], get_places_by_city.to_toolkit()[0]]

# def convert_to_tool(tool_fn):
#     return tool_fn.to_toolkit()[0]

# tools = [convert_to_tool(get_cities), convert_to_tool(get_places_by_city)]


# city_planner_agent = Agent(
#     role="City Planner",
#     goal="Help tourists explore Algeria with personalized and rich recommendations",
#     backstory="You're a travel expert for Algeria with deep knowledge of cities, places, and cultural heritage.",
#     tools=tools,
#     allow_delegation=False,
#     llm=llm,
#     verbose=True
# )


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
