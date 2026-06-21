# Libraries - offline
import streamlit as st
import time
from src.rag.rag_service import ask_opsmind
from src.rag.splitter import split_documents
from src.rag.vectorstore import (create_vectorstore, load_vectorstore)
from src.rag.knowledge_manager import (build_or_update_knowledge_base)
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
import os

# Initialize session state early
if "messages" not in st.session_state:
    st.session_state.messages = []

#Confiure page - better Layout
st.set_page_config(
    page_title="OpsMind AI",
    page_icon="🤖",
    layout="wide"
)
# Header
st.title("OpsMind AI - Offline Operations Assistant")
st.caption("Runs completely on your machine")
# NAV BAR
st.sidebar.title("Knowledge base")
if Path("vectorstore").exists():
    st.sidebar.success("Knowledge based loaded")
else:
    st.warning(
            "No knowlege base found. Upload document to create one."
        )

# Document Upload Module
    st.sidebar.subheader("Upload Document(s)")

    uploaded_files = st.file_uploader(
        "Upload Organisational Documents",
        type=["pdf"],
        accept_multiple_files=True
        )

# Columns
left_col, right_col = st.columns(
    [1,2]
)
#LEFT PANEL
with left_col:
    st.subheader(
        "Knowledge Base"
    )
    # Check if vectorstore exists
    if Path("vectorstore").exists():
        st.success("✅ Knowledge base ready")
    else:
        st.info("📂 No knowledge base yet. Upload PDFs to create one.")

    # Document Upload Module
    st.subheader("Upload Document(s)")

    uploaded_files = st.file_uploader(
        "Upload Organisational Documents",
        type=["pdf"],
        accept_multiple_files=True
        )

    # Display Uploaded document
    uploaded_folder = Path(
        "data/uploads"
    )
    if uploaded_folder.exists():
        files = list(
            uploaded_folder.glob("*.pdf")
        )
        st.sidebar.subheader(
            "Documents"
                            )
        st.sidebar.metric(
            "Total Documents",
            len(files)
        )
        for file in files:
            st.sidebar.write(
                f"📄 {file.name}"
            )


    # Process uploaded file (Offline pipeline)
    if uploaded_files:
        # Save the uploaded file to a temporary location
        os.makedirs("data/uploads", exist_ok=True)

        all_docs = []

        for uploaded_file in uploaded_files:
            file_path = (
                f"data/uploads/{uploaded_file.name}"
            )
            if not Path(file_path).exists():
                with open(
                    file_path,
                    "wb"
                ) as f:
                    f.write(
                        uploaded_file.getbuffer()
                    )

            # Load + Split + Index    
            loader = PyPDFLoader(
                file_path
            )
            docs = loader.load()
            all_docs.extend(docs)

        chunks = split_documents(
            all_docs
        )
        start = time.time()
        db = build_or_update_knowledge_base(
            chunks
            )
        elapsed = time.time() - start
        st.success(
        f"{len(uploaded_files)} document (s) added to knowlege base in {elapsed:.2f} seconds")


# RIGHT PANEL
with right_col:

    st.subheader(
        "Ask OpsMind"
    )
    question = st.text_input(
        "Ask a question about your documents:",
        placeholder="e.g., What are the operational procedures?",
        key="question_input"
    )
    if st.button("🔍 Ask", use_container_width=True):
        if question:
            with st.spinner("OpsMind is thinking..."):
                result = ask_opsmind(question)
            
            # Save to chat history
            st.session_state.messages.append({"role": "user", "content": question})
            st.session_state.messages.append({"role": "assistant", "content": result["answer"]})
            st.rerun()
        else:
            st.warning("Please enter a question!")
    
    # Display chat history in the right column
    if st.session_state.messages:
        st.divider()
        st.subheader("📝 Conversation History")
        
        # Display in reverse order (newest first)
        # Loop through the list backwards, jumping by 2 elements at a time
        # This grabs the start index of each "User + Assistant" pair
        for i in range(len(st.session_state.messages) - 2, -1, -2):
            try:
                user_msg = st.session_state.messages[i]
                bot_msg = st.session_state.messages[i + 1]
                
                # 1. Display the User prompt first
                st.markdown(f"**You:** {user_msg['content']}")
                
                # 2. Display the OpsMind response right below it
                st.markdown(f"**OpsMind:** {bot_msg['content']}")
                with st.expander("📚 View Answer Details"):
                    st.write(bot_msg['content'])
                    
                # Add a visual separator line between different chat turns
                st.divider()
                
            except IndexError:
                # Prevents crashes if a conversation block is incomplete
                pass

        
        # Clear history button
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
