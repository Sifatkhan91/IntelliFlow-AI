from app.agents.graph import build_graph

agent = build_graph()

response = agent.invoke(
    {
        "question":
        "analyze this document"
    }
)

print("\nAGENT RESPONSE:\n")

print(response["answer"])