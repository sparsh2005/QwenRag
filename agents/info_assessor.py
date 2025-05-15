from crewai import CrewAgent

info_assessor = CrewAgent(
    role="Information Assessor",
    goal="Determine whether external information is needed to complete the task.",
    backstory=(
        "You assess whether the current knowledge is sufficient or if more context must be retrieved from external sources."
    ),
    verbose=True
)
