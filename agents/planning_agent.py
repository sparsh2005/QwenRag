from crewai import Agent
from crewai.tools.base_tool import Tool
from typing import List, Dict
import os

def plan_retrieval_strategy(sub_queries: List[str]) -> Dict[str, List[str]]:
    """
    Plan the retrieval strategy for each sub-query.
    Returns a dictionary mapping each sub-query to a list of retrieval methods.
    
    Args:
        sub_queries (List[str]): List of sub-queries to plan retrieval for
        
    Returns:
        Dict[str, List[str]]: Dictionary mapping each sub-query to its retrieval methods
    """
    # For testing, use a simple strategy
    strategy = {}
    for query in sub_queries:
        if "compare" in query.lower() or "difference" in query.lower():
            strategy[query] = ["web_search", "vector_db"]
        else:
            strategy[query] = ["vector_db"]
    return strategy

planning_tool = Tool(
    name="RetrievalPlanningTool",
    func=plan_retrieval_strategy,
    description="Plan the optimal retrieval strategy for each sub-query"
)

planning_agent = Agent(
    role="Retrieval Planning Agent",
    goal="Create an optimal retrieval strategy for each sub-query",
    backstory=(
        "You are an expert at planning information retrieval strategies. "
        "You understand when to use web search vs. vector DB, and how to "
        "combine multiple retrieval methods for comprehensive results."
    ),
    tools=[planning_tool],
    allow_llm=True,
    verbose=True,
    llm_config={
        "provider": "openrouter",
        "model": "qwen/qwen-72b-chat",
        "api_key": os.getenv("OPENROUTER_API_KEY")
    }
) 