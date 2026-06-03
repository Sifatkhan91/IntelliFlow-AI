from typing import TypedDict


class AgentState(TypedDict):

    question: str

    intent: str

    retrieved_docs: str

    answer: str

    analysis: str