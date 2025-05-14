# Agentic RAG system powered by Qwen, CrewAI, Firecrawl, and Qdrant
🧠 What Does QwenRag Do?
QwenRag is an Agentic RAG system — a smarter, more dynamic version of Retrieval-Augmented Generation — that uses multiple AI agents working together to answer complex questions using real-time web data and local memory.

💬 In simple terms:
“It’s like ChatGPT with a brain team. Each AI agent has a specific job — some search the web, some fetch from memory, others judge the answers — and they all collaborate to give the best possible answer.”

📌 Example
You ask:
"Summarize the latest news on electric vehicles and give investment insights."

Here’s what happens inside QwenRag:

📝 Query Rewriter Agent
Rewrites your question to be clearer and search-friendly.

🔍 Info Assessor Agent
Decides:

“Do I already know enough?”
If not…

🌐 Retriever Agent
Uses Firecrawl to search the live web for news articles
and Qdrant to fetch info from stored documents.

🧠 Response Generator Agent
Uses Qwen, a powerful local LLM, to read all the data and write a high-quality response.

✅ Evaluator Agent
Checks if the answer is accurate and complete.
If not, it loops the process again.

🔄 What Makes QwenRag Special?
It plans, retrieves, generates, and refines — like a team of mini-AIs.

Unlike normal RAG systems, it doesn’t stop after one shot. It iterates until it’s confident.

It uses real-time data and memory, not just static training.

🤖 Real-World Use Cases
Smart research assistants

Market analysis bots

AI journalists or writers

Code troubleshooting bots

Decision-making copilots for business