
from crewai import CrewAgent

# This agent rewrites or refines the user's query
query_rewriter = CrewAgent(
    role="Query Rewriter",
    goal="Improve and rewrite the user query for better context understanding and retrieval.",
    backstory=(
        "You're an expert at refining natural language queries into more specific and useful formats for AI understanding."
    ),
    allow_llm=True,
    verbose=True
)
