from crewai import Crew, Task

# Import agents
from agents.query_rewriter import query_rewriter
from agents.info_assessor import info_assessor
from agents.retriever_agent import retriever_agent
from agents.response_generator import response_generator
from agents.response_evaluator import response_evaluator

def main():
    print("🤖 Welcome to QwenRag: Your Agentic RAG System")
    user_query = input("🧠 Ask me anything: ")

    # Define tasks for each agent
    task1 = Task(
        description=f"Rewrite the user's query for better retrieval. Original query: {user_query}",
        expected_output="A refined, specific version of the query",
        agent=query_rewriter
    )

    task2 = Task(
        description="Evaluate whether more external information is needed for the refined query",
        expected_output="YES or NO, along with reasoning",
        agent=info_assessor
    )

    task3 = Task(
        description="If more info is needed, retrieve relevant data from the web or a vector DB",
        expected_output="Relevant information that helps answer the refined query",
        agent=retriever_agent
    )

    task4 = Task(
        description="Use the refined query and retrieved context (if any) to generate a full response",
        expected_output="A complete and useful answer to the original user query",
        agent=response_generator
    )

    task5 = Task(
        description="Review and critique the generated response for completeness and quality",
        expected_output="Improved version of the response if needed",
        agent=response_evaluator
    )

    # Create the Crew and run the process
    crew = Crew(
        agents=[
            query_rewriter,
            info_assessor,
            retriever_agent,
            response_generator,
            response_evaluator
        ],
        tasks=[task1, task2, task3, task4, task5],
        verbose=True
    )

    final_output = crew.kickoff()
    print("\n✅ Final Answer:\n", final_output)

if __name__ == "__main__":
    main()