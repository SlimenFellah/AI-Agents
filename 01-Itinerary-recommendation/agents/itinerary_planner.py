from crewai import Agent

def get_itinerary_planner(llm):
    return Agent(
        role="Itinerary Planner",
        goal="Build travel itineraries based on tourist preferences",
        backstory="Seasoned trip planner who knows Algeria well",
        llm=llm,
        verbose=True
    )
