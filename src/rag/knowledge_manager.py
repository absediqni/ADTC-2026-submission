from pathlib import Path
from src.rag.vectorstore import (
    create_vectorstore,
    load_vectorstore,
    save_vectorstore
)

#Configure path
VECTORSTORE_PATH = "vectorstore"

def build_or_update_knowledge_base(chunks):
    """
    Create a new FAISS index if one does not exist,
    Otherwise append new chunks to the existing index.
    """
    if Path (VECTORSTORE_PATH).exists():
        db = load_vectorstore(VECTORSTORE_PATH)
        db.add_documents(chunks)
        save_vectorstore(
            db, VECTORSTORE_PATH
        )
        return db
    
    db = create_vectorstore(
            chunks
            )
    save_vectorstore(
            db, VECTORSTORE_PATH
        )
    return db