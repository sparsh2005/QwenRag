from dotenv import load_dotenv
load_dotenv()
from crewai import Crew, Task
import os

# Import agents
from agents.query_rewriter import query_rewriter
from agents.planning_agent import planning_agent
from agents.info_assessor import info_assessor
from agents.retriever_agent import retriever_agent
from agents.response_generator import response_generator
from agents.response_evaluator import response_evaluator

# Optional: Add some seed documents to the Qdrant vector DB
from vector_db.qdrant_client import add_to_qdrant

def main():
    print("🤖 Welcome to QwenRag: Your Agentic RAG System")
    user_query = input("🧠 Ask me anything: ")

    # Optional: Sample documents to populate the vector DB
    sample_docs = [
        "Agentic RAG allows dynamic, multi-step reasoning using retrieval and planning agents.",
        "Qwen is a multilingual, locally run LLM developed by Alibaba.",
        "Qdrant is an open-source vector database used for semantic search and storage."
    ]
    add_to_qdrant(sample_docs)

    # Define tasks for each agent
    task1 = Task(
        description=f"Decompose the user's query into sub-queries. Original query: {user_query}",
        expected_output="A list of focused sub-queries",
        agent=query_rewriter
    )

    task2 = Task(
        description="Create a retrieval strategy for each sub-query",
        expected_output="A plan specifying which retrieval methods to use for each sub-query",
        agent=planning_agent
    )

    task3 = Task(
        description="Evaluate whether more external information is needed for each sub-query",
        expected_output="YES or NO for each sub-query, along with reasoning",
        agent=info_assessor
    )

    task4 = Task(
        description="Retrieve relevant data for each sub-query based on the plan",
        expected_output="Relevant information for each sub-query",
        agent=retriever_agent
    )

    task5 = Task(
        description="Synthesize all retrieved information into a coherent response",
        expected_output="A complete and well-structured answer to the original query",
        agent=response_generator
    )

    task6 = Task(
        description="Review and critique the generated response for completeness and quality",
        expected_output="Improved version of the response if needed",
        agent=response_evaluator
    )

    # Create the Crew and run the process
    crew = Crew(
        agents=[
            query_rewriter,
            planning_agent,
            info_assessor,
            retriever_agent,
            response_generator,
            response_evaluator
        ],
        tasks=[task1, task2, task3, task4, task5, task6],
        verbose=True,
        llm_config={
            "provider": "openrouter",
            "model": "qwen/qwen-72b-chat",
            "api_key": os.getenv("OPENROUTER_API_KEY")
        }
    )

    final_output = crew.kickoff()
    print("\n✅ Final Answer:\n", final_output)

if __name__ == "__main__":
    main()