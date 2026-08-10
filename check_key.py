import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Grab the key from the environment
key = os.getenv("GEMINI_API_KEY")

print("--- KEY DIAGNOSTIC REPORT ---")
if not key:
    print("RESULT: GEMINI_API_KEY is empty or not found!")
else:
    print(f"Total Character Length: {len(key)}")
    print(f"First 6 characters: {key[:6]}")
    print(f"Last 4 characters: {key[-4:]}")
    
    if key.startswith("AIzaSy"):
        print("PREFIX CHECK: PASSED (Starts with AIzaSy)")
    else:
        print("PREFIX CHECK: FAILED (Does NOT start with AIzaSy!)")
        
    if "YOUR_ACTUAL" in key or "placeholder" in key:
        print("WARNING: You left a placeholder text in your key!")
print("-----------------------------")