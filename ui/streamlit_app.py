import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

from app.agents.graph import build_graph

# Build agent once
agent = build_graph()

# Page config
st.set_page_config(
    page_title="IntelliFlow AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 IntelliFlow AI")

st.markdown("""
### Multi-Agent AI Assistant

Features:

- QA Agent
- Summary Agent
- Analytics Agent
- Gemini Router
- LangGraph Workflow
- ChromaDB Retrieval
- Conversation Memory
""")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Ask a question about your documents...")

if prompt:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Agent processing
    with st.spinner("Thinking..."):

        response = agent.invoke(
            {
                "question": prompt
            }
        )

        answer = response["answer"]

    # Show assistant response
    with st.chat_message("assistant"):
        st.markdown(answer)

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )