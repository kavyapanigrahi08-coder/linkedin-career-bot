import os
from dotenv import load_dotenv
from google import genai

# Explicitly load .env file
load_dotenv()

class AIEngine:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        
        if not self.api_key:
            print("--- DEBUG INFO ---")
            print("Current working directory files:", os.listdir("."))
            print("------------------")
            raise ValueError("CRITICAL: GEMINI_API_KEY is missing from environment variables.")
        
        self.client = genai.Client(api_key=self.api_key)

    def generate_response(self, prompt: str, system_instruction: str = None) -> str:
        try:
            config = {}
            if system_instruction:
                config["system_instruction"] = system_instruction

            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config=config if config else None
            )
            return response.text
        except Exception as e:
            raise RuntimeError(f"Gemini API Error: {str(e)}")