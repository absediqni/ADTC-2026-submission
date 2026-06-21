from src.rag.vectorstore import load_vectorstore


# Cache vectorstore in memory for faster retrievals
_cached_vectorstore = None


def retrieve_documents(
    question: str,
    k: int = 2
):
    """
    Retrieve documents from vectorstore using similarity search.
    Uses in-memory caching to avoid reloading the vectorstore on each query.
    """
    global _cached_vectorstore
    
    # Load vectorstore only if not cached
    if _cached_vectorstore is None:
        _cached_vectorstore = load_vectorstore()
    
    db = _cached_vectorstore

    return db.similarity_search(
        question,
        k=k
    )