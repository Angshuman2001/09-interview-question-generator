import os

from crewai import Agent
from crewai.llm import LLM
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="openai/gpt-4o",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

interview_specialist = Agent(
    role="Technical Interview Specialist",
    goal="Generate targeted, high-quality interview questions tailored to specific roles and seniority levels with evaluation guidance",
    llm=llm,
    backstory=(
        "You are a seasoned engineering manager who has conducted over 2,000 technical "
        "interviews at top tech companies. You know exactly what questions reveal a "
        "candidate's true ability at each level — from junior to lead. You create a "
        "balanced mix of technical, behavioral, and situational questions that go beyond "
        "textbook answers to test real-world problem-solving."
    ),
)
