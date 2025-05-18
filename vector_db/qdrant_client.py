from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer
import hashlib

# Load embedder (use lightweight model to start)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize Qdrant client (in-memory DB)
client = QdrantClient(":memory:")

# Create collection
collection_name = "knowledge_base"

def create_collection():
    if collection_name not in client.get_collections().collections:
        client.recreate_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE)
        )

def embed_text(text: str):
    return model.encode(text).tolist()

def add_to_qdrant(texts: list[str]):
    create_collection()
    points = [
        PointStruct(
            id=int(hashlib.md5(t.encode()).hexdigest(), 16) % 10**12,
            vector=embed_text(t),
            payload={"content": t}
        )
        for t in texts
    ]
    client.upsert(collection_name=collection_name, points=points)

def search_qdrant(query: str, top_k: int = 3) -> str:
    query_vector = embed_text(query)
    hits = client.search(
        collection_name=collection_name,
        query_vector=query_vector,
        limit=top_k
    )
    return "\n\n".join([hit.payload["content"] for hit in hits])