# Create FAISS Vector Store
from langchain_community.vectorstores import FAISS
from src.rag.embeddings import get_embeddings

def create_vectorstore(chunks: list):
    """
    Create a FAISS index from document chunks.
    """
    embeddings = get_embeddings()

    db = FAISS.from_documents(
                             documents=chunks,
                                embedding=embeddings
                                )
    return db

def save_vectorstore(db, path: str = "vectorstore"):
    """
    Persist FAISS index locally.
    """
    db.save_local(path)


def load_vectorstore(path: str = "vectorstore"):
    """
    Load a FAISS index from disk.
    """
    embeddings = get_embeddings()

# Change 'allow_dangerous_code_execution' to 'allow_dangerous_code_execution' to True to allow loading of FAISS index with custom code.
    db = FAISS.load_local(
        path,
        embeddings,
        allow_dangerous_deserialization=True)
    return db
