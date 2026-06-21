from src.rag.splitter import split_documents
from src.rag.vectorstore import create_vectorstore, save_vectorstore
from langchain_community.document_loaders import PyPDFLoader

# Load PDF
loader = PyPDFLoader("data/documents/sample.pdf")
docs = loader.load()

# Split
chunks = split_documents(docs)

# Create vectorstore
db = create_vectorstore(chunks)

# Save vectorstore to disk
save_vectorstore(db, path="vectorstore")

print("Saved vectorstore to 'vectorstore/'")
