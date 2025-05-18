from crewai import CrewAgent
from crewai_tools import Tool

from retriever.firecrawl_retriever import search_web

web_search_tool = Tool(
    name="WebSearchTool",
    func=search_web,
    description="Use this tool to search the web and retrieve fresh, relevant information."
)

retriever_agent = CrewAgent(
    role="Retriever Agent",
    goal="Fetch relevant information from a vector database or the web using search tools.",
    backstory=(
        "You're skilled in searching the web to fetch documents and relevant snippets that help answer the given task."
    ),
    tools=[web_search_tool],
    verbose=True
)