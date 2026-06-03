from langgraph.graph import StateGraph

from app.agents.state import AgentState

import app.agents.nodes as nodes


def build_graph():

    graph = StateGraph(AgentState)

    graph.add_node(
        "router",
        nodes.router_node
    )

    graph.add_node(
        "retrieve",
        nodes.retrieve_node
    )

    graph.add_node(
        "answer",
        nodes.answer_node
    )

    graph.add_node(
        "summary",
        nodes.summary_node
    )

    graph.add_node(
        "analytics",
        nodes.analytics_node
    )

    graph.set_entry_point(
        "router"
    )

    graph.add_conditional_edges(
        "router",
        nodes.route_decision,
        {
            "qa": "retrieve",
            "summary": "summary",
            "analytics": "analytics"
        }
    )

    graph.add_edge(
        "retrieve",
        "answer"
    )

    graph.set_finish_point(
        "answer"
    )

    graph.set_finish_point(
        "summary"
    )

    graph.set_finish_point(
        "analytics"
    )

    return graph.compile()