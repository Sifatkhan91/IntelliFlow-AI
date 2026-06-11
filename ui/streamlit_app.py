import sys
from pathlib import Path

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)


import sys
from pathlib import Path

import streamlit as st
from app.tools.dashboard_tool import (
    get_dashboard_data
)
st.title("🤖 IntelliFlow AI")

# ----------------------------------
# Dashboard Analytics
# ----------------------------------

dashboard = get_dashboard_data()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Documents",
        dashboard["documents"]
    )

with col2:
    st.metric(
        "Chunks",
        dashboard["chunks"]
    )

with col3:
    st.metric(
        "Words",
        dashboard["words"]
    )

with col4:
    st.metric(
        "Conversations",
        dashboard["conversations"]
    )

st.divider()

# ----------------------------------
# Project Path
# ----------------------------------

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)

# ----------------------------------
# Imports
# ----------------------------------

from app.agents.graph import build_graph

from app.rag.ingest import ingest_document

from app.rag.vectorstore import collection

from app.memory.memory_manager import (
    load_memory,
    clear_memory
)

# ----------------------------------
# Build Agent
# ----------------------------------

agent = build_graph()

# ----------------------------------
# Page Config
# ----------------------------------

st.set_page_config(
    page_title="IntelliFlow AI",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------------
# Header
# ----------------------------------

st.title("🤖 IntelliFlow AI")

st.markdown("""
### Multi-Agent AI Assistant

Features:

- QA Agent
- Summary Agent
- Analytics Agent
- OpenAI Router
- LangGraph Workflow
- ChromaDB Retrieval
- Persistent Memory
- File Upload
""")

# ----------------------------------
# Sidebar
# ----------------------------------

with st.sidebar:

    st.header("📂 Upload Document")

    uploaded_file = st.file_uploader(
        "Choose a file",
        type=[
            "pdf",
            "docx",
            "txt",
            "csv"
        ]
    )

    if uploaded_file:

        uploads_dir = Path(
            "uploaded_docs"
        )

        uploads_dir.mkdir(
            exist_ok=True
        )

        save_path = (
            uploads_dir
            / uploaded_file.name
        )

        with open(
            save_path,
            "wb"
        ) as f:

            f.write(
                uploaded_file.getbuffer()
            )

        if st.button(
            "Process Document"
        ):

            try:

                chunk_count = ingest_document(
                    str(save_path)
                )

                st.success(
                    f"Document processed successfully! {chunk_count} chunks added."
                )

            except Exception as e:

                st.error(
                    str(e)
                )

    st.divider()

    # ----------------------------------
    # Documents List
    # ----------------------------------

    try:

        data = collection.get()

        documents = sorted(
            list(
                set(
                    [
                        item["source"]
                        for item in data["metadatas"]
                    ]
                )
            )
        )

    except Exception:

        documents = []

    active_document = st.selectbox(
        "Select Document",
        options=documents
        if documents
        else ["No Documents"]
    )

    st.divider()

    # ----------------------------------
    # Memory
    # ----------------------------------

    memory = load_memory()

    st.caption(
        f"🧠 Memory Entries: {len(memory)}"
    )

    if st.button(
        "🗑 Clear Memory"
    ):

        clear_memory()

        st.success(
            "Memory cleared successfully."
        )

    st.divider()

    # ----------------------------------
    # Memory Viewer
    # ----------------------------------

    with st.expander(
        "🧠 Conversation Memory"
    ):

        memory = load_memory()

        if not memory:

            st.info(
                "No memory stored yet."
            )

        else:

            for item in reversed(
                memory[-20:]
            ):

                st.markdown(
                    f"**Q:** {item['question']}"
                )

                st.markdown(
                    f"**A:** {item['answer']}"
                )

                st.divider()

# ----------------------------------
# Chat History
# ----------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []

# ----------------------------------
# Display Messages
# ----------------------------------

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

# ----------------------------------
# Chat Input
# ----------------------------------

prompt = st.chat_input(
    "Ask a question about your documents..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message(
        "user"
    ):

        st.markdown(
            prompt
        )

    with st.spinner(
        "Thinking..."
    ):

        response = agent.invoke(
            {
                "question": prompt,
                "active_document": active_document
            }
        )

        answer = response[
            "answer"
        ]

    with st.chat_message(
        "assistant"
    ):

        st.markdown(
            answer
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )