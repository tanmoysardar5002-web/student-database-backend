from google import genai

from app.core.config import GEMINI_API_KEY, GEMINI_MODEL


def ask_gemini(question: str, database_context: str) -> str:
    if not GEMINI_API_KEY:
        return "Gemini API is not configured. Please add GEMINI_API_KEY to the .env file."

    client = genai.Client(api_key=GEMINI_API_KEY)

    prompt = f"""
You are an AI Student Database Assistant.

Answer questions using only the student database information below.
Do not invent students, CGPA values, courses, emails, or other database information.
If the requested information is not available, say so clearly.
Do not reveal student email addresses unless the user explicitly asks for an email.

Student Database:
{database_context}

User Question:
{question}

Give a clear and concise answer.
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
    )
    return response.text or "Gemini returned an empty response."
