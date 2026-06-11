from typing import TypedDict, List


class AgentState(TypedDict, total=False):

    question: str

    intent: str

    answer: str

    retrieved_docs: str

    memory_context: str

    sources: List[str]

    active_document: str

    metadata: list