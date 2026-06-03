from app.rag.retriever import retrieve_relevant_chunks

from app.services.llm_service import ask_gemini

from app.agents.analytics_agent import analyze_document


def router_node(state):

    question = state["question"].lower()

    if "summarize" in question:

        intent = "summary"

    elif "analyze" in question:

        intent = "analytics"

    else:

        intent = "qa"

    return {
        "intent": intent
    }


def summary_node(state):

    docs = retrieve_relevant_chunks(
        state["question"],
        top_k=5
    )

    context = "\n\n".join(docs)

    prompt = f"""
Summarize the following content clearly.

Content:

{context}

Summary:
"""

    summary = ask_gemini(prompt)

    return {
        "answer": summary
    }


def analytics_node(state):

    docs = retrieve_relevant_chunks(
        state["question"],
        top_k=5
    )

    context = "\n\n".join(docs)

    result = analyze_document(context)

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

Use ONLY the context below.

Context:

{state['retrieved_docs']}

Question:

{state['question']}

Answer:
"""

    answer = ask_gemini(prompt)

    return {
        "answer": answer
    }


def route_decision(state):

    return state["intent"]