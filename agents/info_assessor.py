from crewai import Agent
import os

info_assessor = Agent(
    role="Information Assessment Agent",
    goal="Evaluate whether additional information is needed for each sub-query",
    backstory=(
        "You are an expert at determining what information is needed to answer questions. "
        "You can quickly assess whether we have enough context or need to search for more."
    ),
    allow_llm=True,
    verbose=True,
    llm_config={
        "provider": "openrouter",
        "model": "qwen/qwen-72b-chat",
        "api_key": os.getenv("OPENROUTER_API_KEY")
    }
)
