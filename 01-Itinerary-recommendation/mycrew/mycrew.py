from crewai import Task, Crew, Process, LLM
from agents.city_explorer import get_city_explorer
from agents.itinerary_planner import get_itinerary_planner

llm = LLM(
    model="ollama/llama2:chat",
    base_url="http://localhost:11434",
    temperature=0.5
)

def build_crew():
    city_explorer = get_city_explorer(llm)
    itinerary_planner = get_itinerary_planner(llm)

    task1 = Task(
        description="List all major Algerian cities and popular places",
        expected_output="List of cities with 2-3 main attractions each",
        agent=city_explorer,
    )

    task2 = Task(
        description="Based on places found, build a 3-day itinerary for a cultural tourist",
        expected_output="Detailed itinerary with day-wise plan",
        agent=itinerary_planner,
    )

    crew = Crew(
        agents=[city_explorer, itinerary_planner],
        tasks=[task1, task2],
        process=Process.sequential,
        verbose=True
    )
    return crew
