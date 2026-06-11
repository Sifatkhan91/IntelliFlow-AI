from app.rag.retriever import retrieve_relevant_chunks

from app.services.openai_service import ask_openai

from app.agents.analytics_agent import analyze_document

from app.agents.router_agent import classify_intent

from app.memory.memory_manager import (
    get_memory_context,
    save_to_memory,
    get_recent_questions
)

from app.tools.document_tool import (
    list_documents
)

from app.tools.memory_tool import (
    memory_summary
)

from app.tools.stats_tool import (
    document_statistics
)


def router_node(state):

    intent = classify_intent(
        state["question"]
    )

    print(
        f"\nROUTER DECISION: {intent}\n"
    )

    return {
        "intent": intent,
        "memory_context": get_memory_context()
    }


def memory_node(state):

    questions = get_recent_questions()

    if not questions:

        return {
            "answer":
            "No conversation history found."
        }

    response = "Recent Questions:\n\n"

    for i, q in enumerate(
        questions,
        start=1
    ):
        response += f"{i}. {q}\n"

    return {
        "answer": response
    }


def documents_tool_node(state):

    result = list_documents()

    return {
        "answer": result
    }


def memory_tool_node(state):

    result = memory_summary()

    return {
        "answer": result
    }


def stats_tool_node(state):

    result = document_statistics()

    return {
        "answer": result
    }


def summary_node(state):

    docs = retrieve_relevant_chunks(
        query=state["question"],
        active_document=state.get(
            "active_document"
        ),
        top_k=5
    )

    context = "\n\n".join(
        docs["documents"]
    )

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
        query=state["question"],
        active_document=state.get(
            "active_document"
        ),
        top_k=5
    )

    context = "\n\n".join(
        docs["documents"]
    )

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

    result = retrieve_relevant_chunks(
        query=state["question"],
        active_document=state.get(
            "active_document"
        )
    )

    return {
        "retrieved_docs":
        "\n\n".join(
            result["documents"]
        ),

        "sources":
        result.get(
            "sources",
            []
        )
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

If the answer is not present in the context,
say exactly:

I could not find this information in the selected document.

Answer:
"""

    answer = ask_openai(
        prompt
    )

    sources = state.get(
        "sources",
        []
    )

    if sources:

        source_text = "\n".join(
            [
                f"📄 {source}"
                for source in sources
            ]
        )

        final_answer = f"""
{answer}

---

Sources:

{source_text}
"""

    else:

        final_answer = answer

    save_to_memory(
        state["question"],
        final_answer
    )

    return {
        "answer": final_answer
    }


def route_decision(state):

    return state["intent"]