# 🗺️ AI Itinerary Recommendation App 

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
└── mycrew/
└── crew.py # Crew setup with tasks and agents


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
