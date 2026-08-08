import os
import time
import requests
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError

load_dotenv()

LOCAL_SERVER_URL = os.getenv("LOCAL_LLM_URL", "http://127.0.0.1:8000/generate")

class UnifiedResponse:
    def __init__(self, text: str, candidates = None):
        self.text = text
        self.candidates = candidates or []

def safe_generate_json(client, model, prompt, config, llm: str = "gemini") -> UnifiedResponse:
    """
    Robust LLM generator with smart rate limit (429) backoff.
    Waits 15s on rate limits to let Gemini sliding window reset cleanly.
    """
    max_retries = 6
    for attempt in range(max_retries):
        try:
            if llm == "gemini":
                response = client.models.generate_content(
                    model=model,
                    contents=prompt,
                    config=config
                )
                return UnifiedResponse(response.text, response.candidates)
            elif llm == "qwen":
                temp = 0.1
                max_tok = 1024
                if config:
                    if hasattr(config, "temperature"):
                        temp = config.temperature or 0.1
                    if hasattr(config, "max_output_tokens"):
                        max_tok = config.max_output_tokens or 1024
                payload = {
                    "prompt": prompt,
                    "max_tokens": max_tok,
                    "temperature": temp
                }

                response = requests.post(LOCAL_SERVER_URL, json=payload, timeout=200)
                response.raise_for_status()

                qwen_text = response.json().get("response", "").strip()
                return UnifiedResponse(qwen_text)

        except APIError as e:
            if e.code in [400, 401, 403]:
                raise e

            is_rate_limit = e.code == 429 or "RESOURCE_EXHAUSTED" in str(e) or "429" in str(e)
            wait_time = max(15, 5 * (attempt + 1)) if is_rate_limit else (2 ** attempt)

            if attempt < max_retries - 1:
                print(f"  ⚠️ Rate Limit / APIError {e.code}. Pausing {wait_time}s for sliding window reset...")
                time.sleep(wait_time)
                continue
            raise e
        except Exception as e:
            is_rate_limit = "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e)
            wait_time = max(15, 5 * (attempt + 1)) if is_rate_limit else (2 ** attempt)

            if attempt < max_retries - 1:
                print(f"  ⚠️ LLM Server/Rate Limit error ({e}). Pausing {wait_time}s...")
                time.sleep(wait_time)
                continue
            raise e

