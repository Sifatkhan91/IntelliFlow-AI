from app.services.openai_service import ask_openai


VALID_INTENTS = [
    "qa",
    "summary",
    "analytics"
]


def classify_intent(question):

    prompt = f"""
You are an intent classifier.

Choose ONLY ONE of these intents:

qa
summary
analytics

Return ONLY the intent word.

Question:
{question}
"""

    try:

        result = ask_openai(prompt)

        result = (
            result
            .strip()
            .lower()
            .replace(".", "")
            .replace(",", "")
            .replace("\n", "")
        )

        if result not in VALID_INTENTS:

            print(
                f"Invalid intent from OpenAI: {result}"
            )

            return "qa"

        return result

    except Exception as e:

        print(
            f"Router Error: {e}"
        )

        return "qa"