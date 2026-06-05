from app.agents.graph import build_graph

agent = build_graph()

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    response = agent.invoke(
        {
            "question": question
        }
    )

    print("\nAssistant:\n")

    print(response["answer"])