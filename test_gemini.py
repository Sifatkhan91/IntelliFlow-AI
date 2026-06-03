import time
from app.services.llm_service import ask_gemini

time.sleep(5)

response = ask_gemini("Explain machine learning in simple words")

print(response)