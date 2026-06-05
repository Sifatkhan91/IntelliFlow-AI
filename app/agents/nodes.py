from app.rag.retriever import retrieve_relevant_chunks

from app.services.openai_service import ask_openai

from app.agents.analytics_agent import analyze_document

from app.agents.router_agent import classify_intent

from app.memory.memory_manager import (
    get_memory_context,
    save_to_memory
)


def router_node(state):

    intent = classify_intent(
        state["question"]
    )

    print(f"\nROUTER DECISION: {intent}\n")

    return {
        "intent": intent,
        "memory_context": get_memory_context()
    }


def summary_node(state):

    docs = retrieve_relevant_chunks(
        state["question"],
        top_k=5
    )

    context = "\n\n".join(docs)

    prompt = f"""
Conversation History:

{state['memory_context']}

Summarize the following content.

Content:

{context}

Summary:
"""

    summary = ask_openai(prompt)

    save_to_memory(
        state["question"],
        summary
    )

    return {
        "answer": summary
    }


def analytics_node(state):

    docs = retrieve_relevant_chunks(
        state["question"],
        top_k=5
    )

    context = "\n\n".join(docs)

    result = analyze_document(
        context
    )

    save_to_memory(
        state["question"],
        result
    )

    return {
        "answer": result
    }


def retrieve_node(state):

    docs = retrieve_relevant_chunks(
        state["question"]
    )

    return {
        "retrieved_docs": "\n\n".join(docs)
    }


def answer_node(state):

    prompt = f"""
You are a helpful assistant.

Conversation History:

{state['memory_context']}

Use ONLY the context below.

Context:

{state['retrieved_docs']}

Question:

{state['question']}

Answer:
"""

    answer = ask_openai(prompt)

    save_to_memory(
        state["question"],
        answer
    )

    return {
        "answer": answer
    }


def route_decision(state):

    return state["intent"]