# RAG Service - This module provides a service for the Retrieval-Augmented Generation (RAG) pipeline.
from src.rag.retriever import retrieve_documents
from src.llm.chat import ask_llm

def ask_opsmind(
        question: str
        ):
    """
    Ask OpsMind a question using the RAG pipeline.
    """
    # 1. Retrieve context from vector store
    docs = retrieve_documents(
        question)

    # 2. Ask the LLM with the retrieved context
    context = "\n\n".join(
        doc.page_content 
        for doc in docs
    )

    answer = ask_llm(question, context)

    return {
        "answer": answer,
        "sources": docs
    }