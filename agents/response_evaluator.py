from crewai import CrewAgent

response_evaluator = CrewAgent(
    role="Response Evaluator",
    goal="Review and evaluate the final response to ensure it is accurate, complete, and meets the user's goal.",
    backstory=(
        "You're a quality assurance agent who ensures the final output is clear, useful, and accurate."
    ),
    allow_llm=True,
    verbose=True
)

