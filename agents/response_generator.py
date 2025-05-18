from crewai import Agent
from crewai.tools.base_tool import Tool
from typing import List, Dict
import os

def synthesize_responses(sub_responses: List[Dict[str, str]]) -> str:
    """
    Synthesize multiple sub-responses into a coherent final response.
    Each sub-response is a dict with 'query' and 'response' keys.
    
    Args:
        sub_responses (List[Dict[str, str]]): List of sub-responses to synthesize
        
    Returns:
        str: A coherent final response combining all sub-responses
    """
    # For testing, just concatenate the responses
    result = []
    for resp in sub_responses:
        result.append(f"Regarding '{resp['query']}':\n{resp['response']}")
    return "\n\n".join(result)

synthesis_tool = Tool(
    name="ResponseSynthesisTool",
    func=synthesize_responses,
    description="Combine multiple sub-responses into a coherent final response"
)

response_generator = Agent(
    role="Response Synthesis Agent",
    goal="Synthesize information from multiple sources into a coherent response",
    backstory=(
        "You are an expert at combining information from multiple sources "
        "into a coherent, well-structured response. You understand how to "
        "maintain logical flow while incorporating diverse information."
    ),
    tools=[synthesis_tool],
    allow_llm=True,
    verbose=True,
    llm_config={
        "provider": "openrouter",
        "model": "qwen/qwen-72b-chat",
        "api_key": os.getenv("OPENROUTER_API_KEY")
    }
)

