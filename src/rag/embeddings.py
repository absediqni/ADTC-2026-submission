# Create Embeddings
from langchain_huggingface import HuggingFaceEmbeddings

# Cache embedding model in memory for faster loading
_cached_embeddings = None


def get_embeddings():
    """
    Lightweight embedding model for offline CPU use.
    Uses in-memory caching to avoid reloading the model on each call.
    """
    global _cached_embeddings
    
    if _cached_embeddings is None:
        _cached_embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
    
    return _cached_embeddings
