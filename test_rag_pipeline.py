from src.rag.splitter import split_documents
from src.rag.vectorstore import create_vectorstore
from src.rag.embeddings import get_embeddings
from langchain_community.document_loaders import PyPDFLoader


# 1. Load PDF
loader = PyPDFLoader("data/documents/sample.pdf")
docs = loader.load()

# 2. Split
chunks = split_documents(docs)

# 3. Create Vector Store
db = create_vectorstore(chunks)

# 4. Test similarity search
query = "What is the approval process?"

results = db.similarity_search(query, k=3)

for r in results:
    print("\n--- CHUNK ---")
    print(r.page_content)