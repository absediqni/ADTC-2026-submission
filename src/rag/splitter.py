# Document Splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def split_documents(docs: list[Document]) -> list[Document]:
    """
    Split documents into semantically meaningful chunks for embedding and retrieval.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50,
        separators=["\n\n", "\n", ".", " ", ")",""]
    )
    chunks = splitter.split_documents(docs)
    return chunks