from app.memory.memory_manager import (
    load_memory
)


def memory_summary():

    memory = load_memory()

    if not memory:

        return (
            "No memory available."
        )

    response = (
        "Recent Discussion:\n\n"
    )

    for i, item in enumerate(
        memory[-10:],
        start=1
    ):

        response += (
            f"{i}. {item['question']}\n"
        )

    return response