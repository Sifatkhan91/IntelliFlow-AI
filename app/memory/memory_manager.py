import json
from pathlib import Path

MEMORY_FILE = "memory.json"


def load_memory():

    if not Path(MEMORY_FILE).exists():
        return []

    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


def save_to_memory(
    question,
    answer
):

    memory = load_memory()

    memory.append(
        {
            "question": question,
            "answer": answer
        }
    )

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            memory,
            f,
            indent=2,
            ensure_ascii=False
        )


def clear_memory():

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump([], f)


def get_memory_context(
    limit=10
):

    memory = load_memory()

    recent = memory[-limit:]

    context = ""

    for item in recent:

        context += (
            f"User: {item['question']}\n"
            f"Assistant: {item['answer']}\n\n"
        )

    return context


def get_recent_questions(
    limit=10
):

    memory = load_memory()

    return [
        item["question"]
        for item in memory[-limit:]
    ]