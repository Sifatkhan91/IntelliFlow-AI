from app.services.openai_service import ask_openai


def classify_intent(question):

    question = question.lower()

    # -------------------------
    # Stats Tool
    # -------------------------

    if any(
        word in question
        for word in [
            "statistics",
            "stats",
            "metrics",
            "document statistics",
            "document stats",
            "show document statistics",
            "show stats"
        ]
    ):
        return "tool_stats"

    # -------------------------
    # Document Tool
    # -------------------------

    if (
        "document" in question
        and any(
            word in question
            for word in [
                "list",
                "loaded",
                "available",
                "show",
                "which"
            ]
        )
    ):
        return "tool_documents"

    # -------------------------
    # Memory Tool
    # -------------------------

    if any(
        phrase in question
        for phrase in [
            "what did we discuss",
            "discussion history",
            "conversation history",
            "conversation summary",
            "recent discussion",
            "what have we discussed"
        ]
    ):
        return "tool_memory"

    # -------------------------
    # Memory Node
    # -------------------------

    if any(
        phrase in question
        for phrase in [
            "what did i ask",
            "previous question",
            "last question",
            "remember"
        ]
    ):
        return "memory"

    # -------------------------
    # Summary
    # -------------------------

    if any(
        word in question
        for word in [
            "summarize",
            "summary",
            "summarise"
        ]
    ):
        return "summary"

    # -------------------------
    # Analytics
    # -------------------------

    if any(
        word in question
        for word in [
            "analyze",
            "analyse",
            "analytics",
            "insights",
            "trends"
        ]
    ):
        return "analytics"

    # -------------------------
    # Default
    # -------------------------

    return "qa"