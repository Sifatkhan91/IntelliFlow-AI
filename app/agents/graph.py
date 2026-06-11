from typing import TypedDict

from langgraph.graph import (
    StateGraph,
    END
)

from app.agents.nodes import (
    router_node,
    retrieve_node,
    answer_node,
    summary_node,
    analytics_node,
    memory_node,
    documents_tool_node,
    memory_tool_node,
    stats_tool_node,
    route_decision
)


class AgentState(TypedDict, total=False):

    question: str

    answer: str

    intent: str

    memory_context: str

    retrieved_docs: str

    sources: list

    active_document: str


def build_graph():

    workflow = StateGraph(
        AgentState
    )

    workflow.add_node(
        "router",
        router_node
    )

    workflow.add_node(
        "retrieve",
        retrieve_node
    )

    workflow.add_node(
        "answer",
        answer_node
    )

    workflow.add_node(
        "summary",
        summary_node
    )

    workflow.add_node(
        "analytics",
        analytics_node
    )

    workflow.add_node(
        "memory",
        memory_node
    )

    workflow.add_node(
        "tool_documents",
        documents_tool_node
    )

    workflow.add_node(
        "tool_memory",
        memory_tool_node
    )

    workflow.add_node(
        "tool_stats",
        stats_tool_node
    )

    workflow.set_entry_point(
        "router"
    )

    workflow.add_conditional_edges(
        "router",
        route_decision,
        {
            "qa": "retrieve",

            "summary": "summary",

            "analytics": "analytics",

            "memory": "memory",

            "tool_documents":
            "tool_documents",

            "tool_memory":
            "tool_memory",

            "tool_stats":
            "tool_stats"
        }
    )

    workflow.add_edge(
        "retrieve",
        "answer"
    )

    workflow.add_edge(
        "answer",
        END
    )

    workflow.add_edge(
        "summary",
        END
    )

    workflow.add_edge(
        "analytics",
        END
    )

    workflow.add_edge(
        "memory",
        END
    )

    workflow.add_edge(
        "tool_documents",
        END
    )

    workflow.add_edge(
        "tool_memory",
        END
    )

    workflow.add_edge(
        "tool_stats",
        END
    )

    return workflow.compile()