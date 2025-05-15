from crewai import CrewAgent

retriever_agent = CrewAgent(
    role="Retriever Agent",
    goal="Fetch relevant information from a vector database or the web using search tools.",
    backstory=(
        "You're skilled in searching databases and the internet to fetch documents that help complete a given task."
    ),
    verbose=True
)

