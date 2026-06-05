from openai import OpenAI

from app.utils.config import OPENAI_API_KEY


client = OpenAI(
    api_key=OPENAI_API_KEY
)


def ask_openai(prompt):

    try:

        response = client.responses.create(
            model="gpt-5-mini",
            input=prompt
        )

        return response.output_text

    except Exception as e:

        return f"OpenAI Error: {str(e)}"