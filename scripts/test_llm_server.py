import os
import requests
from dotenv import load_dotenv
from local_llm_client import query_local_llm

load_dotenv()

print("=" * 65)
print(" 🚀 TESTING GATESTER FINE-TUNED KAGGLE GPU SERVER CONNECTIVITY ")
print("=" * 65)

local_url = os.getenv("LOCAL_LLM_URL", "")

print(f"📌 Configured LOCAL_LLM_URL: '{local_url}'\n")

if not local_url:
    print("⚠️ WARNING: LOCAL_LLM_URL is missing in your .env file!")
    print("Set LOCAL_LLM_URL=https://...trycloudflare.com/generate in your .env file.")
    exit(1)

sample_question = """EXPLAIN ABOUT DISK SCHEDULING..."""

print(f"📝 Sending Test Question to Fine-Tuned Kaggle Model:\n")
print(f"Question:\n{sample_question}\n")
print("-" * 65)

try:
    response = query_local_llm(sample_question, max_tokens=512, temperature=0.1, preference="qwen")
    print("\n🤖 FINE-TUNED MODEL BLUEPRINT RESPONSE FROM KAGGLE:\n")
    print(response)
    print("\n" + "=" * 65)
    print("✅ TEST SUCCESSFUL! Kaggle Server is responding with your fine-tuned model!")
    print("=" * 65)
except Exception as e:
    print(f"\n❌ Test Failed: {e}")
