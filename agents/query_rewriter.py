from crewai import Agent
from crewai.tools.base_tool import Tool
import os

def decompose_query(query: str) -> list[str]:
    """
    Decompose a complex query into sub-queries.
    
    Args:
        query (str): The complex query to decompose
        
    Returns:
        list[str]: List of simpler sub-queries
    """
    # For testing, just split on 'and' or return the query
    if " and " in query:
        return [q.strip() for q in query.split(" and ")]
    return [query]

query_decomposition_tool = Tool(
    name="QueryDecompositionTool",
    func=decompose_query,
    description="Break down complex queries into simpler sub-queries"
)

# This agent rewrites or refines the user's query
query_rewriter = Agent(
    role="Query Decomposition Agent",
    goal="Break down complex queries into simpler, focused sub-queries",
    backstory=(
        "You are an expert at analyzing complex questions and breaking them down into "
        "simpler, more focused sub-queries that can be answered independently. "
        "You understand how to maintain the original intent while making queries more specific."
    ),
    tools=[query_decomposition_tool],
    allow_llm=True,
    verbose=True,
    llm_config={
        "provider": "openrouter",
        "model": "qwen/qwen-72b-chat",
        "api_key": os.getenv("OPENROUTER_API_KEY")
    }
)
