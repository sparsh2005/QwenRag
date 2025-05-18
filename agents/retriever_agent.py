from crewai import CrewAgent
from crewai_tools import Tool
from retriever.firecrawl_retriever import search_web
from retriever.qdrant_retriever import search_local_knowledge

web_search_tool = Tool(
    name="WebSearchTool",
    func=search_web,
    description="Search the live web for relevant information"
)

qdrant_tool = Tool(
    name="VectorSearchTool",
    func=search_local_knowledge,
    description="Search local knowledge base (vector database) for relevant context"
)

retriever_agent = CrewAgent(
    role="Retriever Agent",
    goal="Fetch relevant information from either the web or the local vector DB",
    backstory=(
        "You are an expert in both real-time web scraping and using a local knowledge base to provide factual, well-supported context."
    ),
    tools=[web_search_tool, qdrant_tool],
    verbose=True
)