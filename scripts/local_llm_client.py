import os 
import requests
from dotenv import load_dotenv
from google import genai

load_dotenv()

LOCAL_SERVER_URL = "http://127.0.0.1:8000/generate"

ai_client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

def query_local_llm(prompt: str, max_tokens: int = 200, temperature: float = 0.1) -> str:
    """
    Queries the local LLM server on port 8000.
    Falls back to Gemini Cloud if the local server is unreachable.
    """

    try: 
        payload = {
            "prompt" : prompt,
            "max_tokens" : max_tokens,
            "temperature" : temperature
        }
        response = requests.post(LOCAL_SERVER_URL, json = payload, timeout = 60)
        if response.status_code == 200:
            return response.json()["response"]
    except Exception as e:
        print(f"Local LLM server offline ({e}). Falling back to Gemini Cloud...")
    
    res = ai_client.models.generate_content(
        model = "gemini-2.0-flash",
        contents = prompt
    )
    return res.text.strip()
