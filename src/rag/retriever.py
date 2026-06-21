from src.rag.vectorstore import load_vectorstore


def retrieve_documents(
    question: str,
    k: int = 4
):

    db = load_vectorstore()

    return db.similarity_search(
        question,
        k=k
    )