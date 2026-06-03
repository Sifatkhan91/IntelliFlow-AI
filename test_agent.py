from app.agents.graph import build_graph

agent = build_graph()

response = agent.invoke(
    {
        "question": "Give me the key findings from this document"
    }
)

print("\nFINAL RESPONSE:\n")

print(response["answer"])