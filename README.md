AI Trip Planner

An AI-powered travel planning assistant that generates personalized trip itineraries using an LLM agent pipeline. The project combines an agentic backend (built around tools, prompt templates, and configurable logic) with a Streamlit front-end for user interaction and a FastAPI backend for serving requests.

Intentions

The goal of this project is to explore how autonomous AI agents can be used to automate real-world planning tasks in this case, travel itineraries — by combining:

LLM-based reasoning to interpret user travel preferences (destination, duration, budget, interests, etc.)
Tool-calling to fetch supporting information (e.g. places, weather, or other external data) needed to build a realistic plan
Structured prompt engineering to keep agent outputs consistent and usable
A simple web interface so the planner is usable by non-technical end users, not just via API calls

This project is part of an ongoing personal portfolio of AI/ML and agentic AI projects, focused on applying LLM agents to practical, everyday use cases.

How It Works:
User Input :— The user provides trip details (e.g. destination, dates, interests) through the Streamlit app (streamlit_app.py).
Agent Pipeline :— The request is passed to the agent (agent/), which uses prompt templates from prompt_library/ to reason about the request and, where needed, invoke tools (tools/) to gather supporting information.
Configuration & Utilities :— App-wide settings live in config/, with shared helper functions in utils/.
Logging & Error Handling :— logger/ and exception/ provide structured logging and centralized error handling across the app.
API Layer :— main.py exposes the planner as a FastAPI service (run via uvicorn main:app), allowing the agent to be used programmatically as well as through the Streamlit UI.
Output :— The agent returns a generated itinerary/plan, which is displayed back to the user through the Streamlit interface.
Tech Stack
Python (managed with uv)
Streamlit (front-end)
FastAPI + Uvicorn (backend API)
LLM-based agent framework (prompt templates + tool calling)
Running the Project
bash
# Activate virtual environment
uv venv env --python cpython-3.14.6-windows-x86_64-none
env\Scripts\activate.bat

# Install dependencies
uv pip install -r requirements.txt

# Run the Streamlit app
streamlit run streamlit_app.py

# Or run the API server
uvicorn main:app --reload --port 8000
Acknowledgements

# Acknowledgements
Built while following along with Krish Naik's YouTube tutorial series, then adapted/extended as a personal project.

# Status

Work in progress  
Open for Public to commit
