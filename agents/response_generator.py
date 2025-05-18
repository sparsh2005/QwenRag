from crewai import CrewAgent

response_generator = CrewAgent(
    role="Response Generator",
    goal="Generate a complete, informative, and accurate answer based on the available information.",
    backstory=(
        "You're an expert language model capable of synthesizing complex knowledge into coherent responses."
    ),
    allow_llm=True,
    verbose=True
)

