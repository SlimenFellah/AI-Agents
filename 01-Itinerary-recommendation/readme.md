# 🗺️ AI Itinerary Recommendation App (CrewAI + Ollama LLaMA2)

An AI-powered travel itinerary recommendation system for Algeria 🇩🇿 using local Large Language Models (LLMs) with **Ollama**, **FastAPI**, **SQLite**, and **CrewAI**.

---

## 📌 Features

- 🧠 **Local LLMs**: Uses **Ollama** models like `llama2`, `mistral`, etc. — no OpenAI key required.
- 🤖 **CrewAI Agents**: Modular agents plan itineraries, select cities, and recommend top destinations.
- 🧳 **Tourism-Focused**: Ideal for exploring Algerian cities with curated highlights.
- ⚡ **FastAPI Backend**: Lightweight API for integration with frontend apps or tools.
- 🗄️ **SQLite Database**: Stores Algerian cities and popular places.

---

## 📁 Project Structure

```
.
├── main.py # FastAPI app entry point
├── requirements.txt
├── readme.md
├── schema.sql # SQL schema for seeding DB
│
├── api/
│ └── routes.py # API route handlers
│
├── db/
│ ├── database.py # SQLite DB connection
│ └── seed.py # Seeds cities and places
│
├── agents/
│ ├── city_planner.py # CrewAI agent for city selection
│ └── destination_guide.py # Agent for recommending highlights
│
└── mycrew/mycrew.py # Crew setup with tasks and agents
```

## 🚀 Getting Started

### 1. Install Requirements

```bash
pip install -r requirements.txt
Make sure Ollama is installed and running locally.
```
2. Start Ollama and Pull a Model
```bash
ollama pull llama2
```

3. Run the FastAPI App
```bash
uvicorn main:app --reload
App will be running at http://127.0.0.1:8000
```
## 🔥 API Endpoint
POST /generate-itinerary
Description: Generates an itinerary with cities and top places in Algeria using LLM agents.

Request:
```bash
{
  "goal": "I want to visit Algeria",
  "preferences": "I like history, architecture, and coastal cities"
}
Response:
{
  "itinerary": {
    "cities": [...],
    "highlights": {
      "Oran": ["Place 1", "Place 2", "Place 3"],
      ...
    }
  }
}
### 📝 Example API Response

```json
{
  "result": {
    "raw": "Day 1:\n\n* Depart from Algiers and drive to Constantine (approximately 4 hours)\n* Visit the Roman ruins of Tipaza and the Casbah of Constantine\n* Spend the night in Constantine\n\nDay 2:\n\n* Drive from Constantine to Oran (approximately 3.5 hours)\n* Visit the Kasbah of Oran, the Museum of Fine Arts, and the Plage de la Ponche\n* Spend the night in Oran\n\nDay 3:\n\n* Drive from Oran to Annaba (approximately 4.5 hours)\n* Visit the Roman ruins of Thamugas and the Casbah of Annaba\n* Spend the night in Annaba\n\nDay 4:\n\n* Drive from Annaba to Tlemcen (approximately 2.5 hours)\n* Visit the Koutoubia Mosque, the Bahri Djemaa, and the Parc de la Roseraie\n* Spend the night in Tlemcen\n\nDay 5:\n\n* Drive from Tlemcen to Batna (approximately 3 hours)\n* Visit the Kalaa des Louizes, the Casbah of Batna, and the Parc de l'Oued Irhoun\n* Spend the night in Batna\n\nDay 6:\n\n* Drive from Batna to Sétif (approximately 4.5 hours)\n* Visit the University of Sétif, the Grand Mosque, and the Cathedral of Sétif\n* Spend the night in Sétif\n\nDay 7:\n\n* Drive from Sétif to Ghardaia (approximately 3.5 hours)\n* Visit the Bahri Djemaa, the Casbah of Ghardaia, and the Parc de l'Oued Sokne\n* Spend the night in Ghardaia\n\nDay 8:\n\n* Drive from Ghardaia to Adrar (approximately 4.5 hours)\n* Visit the Ksar of Adrar, the Casbah of Adrar, and the Parc National de l'Adrar\n* Spend the night in Adrar\n\nThis itinerary provides a good balance between history, culture, and natural beauty, while also allowing for some flexibility in case of unexpected delays or changes in travel plans. Additionally, it takes into account the distance between each destination to ensure that travel time is minimized and that the trip remains enjoyable and stress-free.",
    "tasks_output": [
      {
        "description": "List all major Algerian cities and popular places",
        "expected_output": "List of cities with 2-3 main attractions each",
        "summary": "List all major Algerian cities and popular places...",
        "raw": "Here are the major cities and popular places in Algeria, along with their top attractions:\n\n1. Algiers - Capital city of Algeria, known for its rich history, cultural landmarks, and bustling markets. Must-visit attractions include the Casbah, the National Museum of Antiquities and Islamic Art, and the Grand Mosque.\n2. Constantine - Located in the northeastern part of Algeria, known for its stunning natural beauty and ancient history. Popular attractions include the Roman ruins of Tipaza, the Casbah of Constantine, and the beautiful beaches along the Mediterranean coast.\n3. Oran - Largest city in Algeria, known for its vibrant cultural scene, beautiful beaches, and rich history. Must-visit attractions include the Kasbah of Oran, the Museum of Fine Arts, and the Plage de la Ponche.\n4. Annaba - Located in the eastern part of Algeria, known for its ancient history, beautiful beaches, and lush greenery. Popular attractions include the Roman ruins of Thamugas, the Casbah of Annaba, and the Plage de la Reine.\n5. Tlemcen - A historic city located in the northwestern part of Algeria, known for its stunning architecture, beautiful parks, and rich cultural heritage. Must-visit attractions include the Koutoubia Mosque, the Bahri Djemaa, and the Parc de la Roseraie.\n6. Batna - Located in the northeastern part of Algeria, known for its natural beauty, historic sites, and vibrant cultural scene. Popular attractions include the Kalaa des Louizes, the Casbah of Batna, and the Parc de l'Oued Irhoun.\n7. Tipaza - A coastal city located in the northwestern part of Algeria, known for its beautiful beaches, historic sites, and rich cultural heritage. Must-visit attractions include the Roman ruins of Tipaza, the Casbah of Tipaza, and the Plage de la Baleine.\n8. Sétif - Located in the northeastern part of Algeria, known for its rich history, cultural landmarks, and vibrant cultural scene. Must-visit attractions include the University of Sétif, the Grand Mosque, and the Cathedral of Sétif.\n9. Ghardaia - Located in the southwestern part of Algeria, known for its stunning architecture, beautiful parks, and rich cultural heritage. Must-visit attractions include the Bahri Djemaa, the Casbah of Ghardaia, and the Parc de l'Oued Sokne.\n10. Adrar - Located in the central part of Algeria, known for its natural beauty, historic sites, and vibrant cultural scene. Popular attractions include the Ksar of Adrar, the Casbah of Adrar, and the Parc National de l'Adrar.\n\nEach of these cities offers a unique blend of history, culture, and natural beauty, making them must-visit destinations for any traveler to Algeria.",
        "agent": "City Explorer"
      },
      {
        "description": "Based on places found, build a 3-day itinerary for a cultural tourist",
        "expected_output": "Detailed itinerary with day-wise plan",
        "summary": "Based on places found, build a 3-day itinerary for a...",
        "raw": "Day 1:\n\n* Depart from Algiers and drive to Constantine (approximately 4 hours)\n* Visit the Roman ruins of Tipaza and the Casbah of Constantine\n* Spend the night in Constantine\n\nDay 2:\n\n* Drive from Constantine to Oran (approximately 3.5 hours)\n* Visit the Kasbah of Oran, the Museum of Fine Arts, and the Plage de la Ponche\n* Spend the night in Oran\n\nDay 3:\n\n* Drive from Oran to Annaba (approximately 4.5 hours)\n* Visit the Roman ruins of Thamugas and the Casbah of Annaba\n* Spend the night in Annaba\n\nDay 4:\n\n* Drive from Annaba to Tlemcen (approximately 2.5 hours)\n* Visit the Koutoubia Mosque, the Bahri Djemaa, and the Parc de la Roseraie\n* Spend the night in Tlemcen\n\nDay 5:\n\n* Drive from Tlemcen to Batna (approximately 3 hours)\n* Visit the Kalaa des Louizes, the Casbah of Batna, and the Parc de l'Oued Irhoun\n* Spend the night in Batna\n\nDay 6:\n\n* Drive from Batna to Sétif (approximately 4.5 hours)\n* Visit the University of Sétif, the Grand Mosque, and the Cathedral of Sétif\n* Spend the night in Sétif\n\nDay 7:\n\n* Drive from Sétif to Ghardaia (approximately 3.5 hours)\n* Visit the Bahri Djemaa, the Casbah of Ghardaia, and the Parc de l'Oued Sokne\n* Spend the night in Ghardaia\n\nDay 8:\n\n* Drive from Ghardaia to Adrar (approximately 4.5 hours)\n* Visit the Ksar of Adrar, the Casbah of Adrar, and the Parc National de l'Adrar\n* Spend the night in Adrar\n\nThis itinerary provides a good balance between history, culture, and natural beauty, while also allowing for some flexibility in case of unexpected delays or changes in travel plans. Additionally, it takes into account the distance between each destination to ensure that travel time is minimized and that the trip remains enjoyable and stress-free.",
        "agent": "Itinerary Planner"
      }
    ],
    "token_usage": {
      "total_tokens": 2653,
      "prompt_tokens": 1191,
      "cached_prompt_tokens": 0,
      "completion_tokens": 1462,
      "successful_requests": 2
    }
  }
}
```
```

## 🧠 Local LLM Setup with CrewAI
We use crewAI's built-in LLM support for Ollama:
from crewai import LLM

llm = LLM(
    model="ollama/llama2",
    base_url="http://localhost:11434",
    temperature=0.5
)
Agents and tasks are defined in agents/ and mycrew/crew.py.

## 🏗️ Future Improvements
 Add frontend UI (React/Vue)

 More detailed filtering (budget, travel days)

 Add multilingual support (Arabic, French)

 User profiles & itinerary storage

## 🧑‍💻 Author
Slimene Fellah
Powered by open-source LLMs & curiosity 
