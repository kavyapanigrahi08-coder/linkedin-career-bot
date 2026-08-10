import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from local .env file if present
load_dotenv()

class AIEngine:
    def __init__(self):
        # Retrieve API key from environment variables (works on local .env & Render)
        self.api_key = os.getenv("GEMINI_API_KEY")
        
        if not self.api_key:
            raise ValueError("CRITICAL: GEMINI_API_KEY is missing from environment variables.")
        
        # Initialize Gemini Client
        self.client = genai.Client(api_key=self.api_key)

    def generate_response(self, prompt: str, system_instruction: str = None) -> str:
        """
        Generates content using the Gemini API model.
        """
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