import time

from google import genai

from app.utils.config import GEMINI_API_KEY


client = genai.Client(
    api_key=GEMINI_API_KEY
)


def ask_gemini(prompt):

    retries = 3

    for attempt in range(retries):

        try:

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            print("\n========== GEMINI ERROR ==========")
            print(type(e))
            print(e)
            print("==================================\n")

            if attempt < retries - 1:

                print(
                    f"Retrying ({attempt + 1}/3)..."
                )

                time.sleep(5)

            else:

                return (
                    f"Gemini Error: {str(e)}"
                )