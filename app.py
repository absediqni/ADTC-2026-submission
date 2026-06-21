# Libraries - offline
import streamlit as st
from src.rag.rag_service import ask_opsmind
from src.rag.splitter import split_documents
from src.rag.vectorstore import create_vectorstore, load_vectorstore
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
import os

#Confiure page
st.set_page_config(
    page_title="Opsmind AI",
    page_icon=":robot_face:",
    layout="wide"
)
st.title("Opsmind AI - Offline Operations Assistant")
st.caption("Runs completely on your machine")

# Document Upload Module
st.header("1. Uploadded Organisational Documents")

uploaded_file = st.file_uploader(
    "Upload Organisational Documents",
    type=["pdf"],
    accept_multiple_files=True
    )

# Process uploaded file (Offline pipeline)
if uploaded_file:
    # Save the uploaded file to a temporary location
    os.makedirs("data/uploads", exist_ok=True)

    file_path = f"data/uploads/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Document uploaded successfully (Stored locally)")

    # Load + Split + Index
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    chunks = split_documents(docs)

    db = create_vectorstore(chunks)
    db.save_local("vectorstore")

    st.success("Document indexed into offline knowledge base")
else:
    st.info("Upload a PDF first to index it into the knowledge base.")

# Qestion Answering Module
st.header("2. Ask OpsMind AI")
question = st.text_input(
    "Ask a quetion about your Organisational documents"
)
if st.button("Ask"):
    if question:
        with st.spinner("OpsMind is thinking ..."):
            result = ask_opsmind(question)
        # Display answer
        st.subheader("Answer")        
        st.markdown(result["answer"])
        # Display Source
        st.subheader("Sources (Local Documents)")
       
        for i, doc in enumerate(result["sources"]):

            source_path = doc.metadata.get(
                "source",
                "Unknown File"
            )

            source_file = Path(
                source_path
            ).name

            page_number = doc.metadata.get(
                "page",
                "Unknown Page"
            )

            with st.expander(
                f"{source_file} | Page {page_number}"
            ):
                st.write(doc.page_content)
