conversation_memory = []


def save_to_memory(question, answer):

    conversation_memory.append(
        {
            "question": question,
            "answer": answer
        }
    )


def get_memory():

    return conversation_memory


def get_memory_context():

    if not conversation_memory:
        return ""

    history = []

    for item in conversation_memory:

        history.append(
            f"""
User: {item['question']}
Assistant: {item['answer']}
"""
        )

    return "\n".join(history)


def clear_memory():

    conversation_memory.clear()