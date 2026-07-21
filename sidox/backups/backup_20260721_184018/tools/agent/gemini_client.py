import os
from google import genai

key = os.getenv("GEMINI_API_KEY")

if not key:
    raise SystemExit("GEMINI_API_KEY not found")

client = genai.Client(api_key=key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Reply with only: Gemini connected successfully."
)

print(response.text)
