from crewai import Agent
import os

response_evaluator = Agent(
    role="Response Evaluation Agent",
    goal="Review and improve the generated response for quality and completeness",
    backstory=(
        "You are an expert at evaluating and improving responses. "
        "You ensure answers are complete, accurate, and well-structured."
    ),
    allow_llm=True,
    verbose=True,
    llm_config={
        "provider": "openrouter",
        "model": "qwen/qwen-72b-chat",
        "api_key": os.getenv("OPENROUTER_API_KEY")
    }
)

