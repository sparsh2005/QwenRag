import os
from dotenv import load_dotenv
from firecrawl import FirecrawlApp

load_dotenv()

firecrawl = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

def search_web(query: str) -> str:
    results = firecrawl.search(query)
    if results and results.get("results"):
        snippets = [r.get("content", "")[:500] for r in results["results"][:3]]
        return "\n\n".join(snippets)
    else:
        return "No relevant web results found."


