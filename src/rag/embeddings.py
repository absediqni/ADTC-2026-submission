# Create Embeddings
from langchain_huggingface import HuggingFaceEmbeddings

def get_embeddings():
    """
    Lightweight embedding model for offline CPU use.
    """
    model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2")
    return model
