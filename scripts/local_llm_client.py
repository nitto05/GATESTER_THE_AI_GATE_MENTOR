import os 
from dotenv import load_dotenv
from google import genai
from api_helper import safe_generate_json

load_dotenv()

ai_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class ConfigMock:
    def __init__(self, temp: float, max_tok: int):
        self.temperature = temp
        self.max_output_tokens = max_tok

def query_local_llm(prompt: str, max_tokens: int = 200, temperature: float = 0.1, preference: str = "qwen") -> str:
    """
    Queries Warm GPU LLM (Qwen) with exponential backoff via safe_generate_json.
    Falls back to Gemini Cloud seamlessly with safe retries if unreachable.
    """
    config = ConfigMock(temperature, max_tokens)
    
    if preference == "qwen":
        try:
            res = safe_generate_json(ai_client, "gemini-2.0-flash", prompt, config=config, llm="qwen")
            if res and res.text:
                return res.text.strip()
        except Exception as e:
            print(f"⚠️ GPU Server unreachable ({e}). Falling back to Gemini Cloud with safe retries...")

    res = safe_generate_json(ai_client, "gemini-2.0-flash", prompt, config=config, llm="gemini")
    return res.text.strip()

