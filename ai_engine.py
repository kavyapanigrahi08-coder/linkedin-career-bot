import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Force load the current .env file over cached session variables
load_dotenv(override=True)

class AIEngine:
    def __init__(self, model: str = "gemini-3.5-flash-lite"):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("CRITICAL: GEMINI_API_KEY is missing from your .env file.")
        
        self.client = genai.Client(api_key=self.api_key)
        self.model = model

    def generate_response(self, system_prompt: str, user_prompt: str, temperature: float = 0.7) -> str:
        try:
            config = types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=temperature,
            )
            input_text = user_prompt.strip() if user_prompt and user_prompt.strip() else "Process using my saved student memory profile."
            
            response = self.client.models.generate_content(
                model=self.model,
                contents=input_text,
                config=config
            )
            return response.text
        except Exception as e:
            return f"[Backend API Error]: Unable to communicate with Gemini.\nDetails: {str(e)}"