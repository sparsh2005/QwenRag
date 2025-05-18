from vector_db.qdrant_client import search_qdrant

def search_local_knowledge(query: str) -> str:
    return search_qdrant(query)
