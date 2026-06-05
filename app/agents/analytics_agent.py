from app.services.openai_service import ask_openai


def analyze_document(text):

    prompt = f"""
You are an AI document analyst.

Analyze the document and provide:

1. Key Insights
2. Important Dates
3. Important Entities
4. Brief Summary

Document:

{text}
"""

    return ask_openai(prompt)