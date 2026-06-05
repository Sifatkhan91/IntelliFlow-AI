from app.services.llm_service import ask_gemini


VALID_INTENTS = [
    "qa",
    "summary",
    "analytics"
]


def classify_intent(question):

    prompt = f"""
You are an intent classifier.

Choose ONLY ONE:

qa
summary
analytics

Return ONLY the word.

Question:
{question}
"""

    try:

        result = ask_gemini(prompt)

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
                f"Invalid intent from Gemini: {result}"
            )

            return "qa"

        return result

    except Exception as e:

        print(
            f"Router Error: {e}"
        )

        return "qa"