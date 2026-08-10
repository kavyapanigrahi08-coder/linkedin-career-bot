import os
from google import genai

# ==================================================
# GEMINI API CONFIGURATION
# ==================================================

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("ERROR: GEMINI_API_KEY is not set.")
    print("Set your API key in the terminal and try again.")
    exit()

# Create Gemini client
client = genai.Client(api_key=API_KEY)

# Gemini model
MODEL = "gemini-3.5-flash-lite"

# ==================================================
# TEST GEMINI
# ==================================================

print("=" * 50)
print("       GEMINI AI TEST")
print("=" * 50)

print("Connecting to Gemini...")
print("Model:", MODEL)

try:

    response = client.models.generate_content(
        model=MODEL,
        contents="Hello Gemini! Introduce yourself in one short sentence."
    )

    print("\nGemini Response:")
    print("-" * 50)
    print(response.text)
    print("-" * 50)

    print("\nSUCCESS: Gemini API is working!")

except Exception as e:

    print("\nGEMINI ERROR:")
    print(e)

print("\nTest finished.")