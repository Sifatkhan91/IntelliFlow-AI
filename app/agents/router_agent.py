from app.services.llm_service import ask_gemini


def classify_intent(question):

    prompt = f"""
You are an intent classifier.

Classify the user request into ONLY ONE of these:

qa
summary
analytics

Rules:

qa = asking questions

summary = requesting summary or overview

analytics = requesting insights, findings, entities, trends, analysis

Return ONLY one word.

Question:

{question}
"""

    result = ask_gemini(prompt)

    return result.strip().lower()