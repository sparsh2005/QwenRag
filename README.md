# QwenRag: Agentic RAG System Powered by Qwen, CrewAI, Firecrawl, and Qdrant

## What is QwenRag?

QwenRag is an intelligent Agentic Retrieval-Augmented Generation (RAG) system. It goes beyond traditional RAG by using a team of collaborative AI agents, each assigned a specific role in solving complex queries. The system integrates real-time web search and long-term memory through vector databases to generate high-quality, context-aware responses.

## How It Works

When a user inputs a question, QwenRag follows a dynamic multi-step process:

1. **Query Rewriter Agent**  
   Refines the user query to improve clarity and search effectiveness.

2. **Information Assessor Agent**  
   Determines whether the system already has enough knowledge to answer or needs to retrieve more information.

3. **Retriever Agent**  
   Searches the live web using Firecrawl and queries stored knowledge from Qdrant, a high-performance vector database.

4. **Response Generator Agent**  
   Synthesizes a complete and well-structured response using the Qwen model accessed via OpenRouter API.

5. **Response Evaluator Agent**  
   Reviews the response to ensure accuracy and completeness. If needed, it triggers another retrieval and generation cycle.

This iterative architecture allows QwenRag to deliver deeper, more accurate, and more reliable answers compared to traditional RAG systems.

## Why QwenRag is Unique

- Built using multiple goal-oriented agents powered by CrewAI.
- Combines live web search with persistent memory through Qdrant.
- Integrates seamlessly with OpenRouter to access Qwen, a state-of-the-art LLM.
- Uses a recursive reasoning loop for refining responses instead of stopping at a single generation.
- Modular and extensible architecture designed for flexibility and scale.

## Use Cases

- Research assistants for technical, scientific, or academic topics
- Market trend analysis and business intelligence
- AI-powered writing and summarization tools
- Automated Q&A systems and expert advisors
- Troubleshooting assistants for developers and engineers

## Project Structure Overview

```
QwenRag/
├── agents/                  # All CrewAI agents and their definitions
├── retriever/               # Web and vector-based search utilities
├── vector_db/               # Qdrant client and vector embedding tools
├── llm/                     # LLM provider logic for OpenRouter or OpenAI
├── main.py                  # Main execution script
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Getting Started

1. Clone the repository
2. Create a virtual environment using Python 3.11
3. Install dependencies from `requirements.txt`
4. Add your API keys to a `.env` file
5. Run `python main.py` and start querying

## License

This project is for educational and experimental use.