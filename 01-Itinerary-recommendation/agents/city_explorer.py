from crewai import Agent

def get_city_explorer(llm):
    return Agent(
        role="City Explorer",
        goal="List cities and major places in Algeria",
        backstory="Expert in Algerian geography and tourism",
        llm=llm,
        verbose=True
    )
