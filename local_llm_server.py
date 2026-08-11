import os
import torch
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from unsloth import FastLanguageModel
import uvicorn

app = FastAPI(title="GateSter Fine-Tuned LLM Server")

# 🔒 Your Fine-Tuned Private Model ID on Hugging Face
MODEL_ID = "nitto05/gatester-stage0-3B"

# Hugging Face Write Token (reads from env variable or fallback)
HF_TOKEN = os.getenv("HF_TOKEN", "your_hf_write_token_here")

print(f"🚀 Loading fine-tuned model '{MODEL_ID}' onto Kaggle GPU...")

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name=MODEL_ID,
    max_seq_length=2048,
    dtype=None,
    load_in_4bit=True,
    token=HF_TOKEN,
    device_map="auto"
)

FastLanguageModel.for_inference(model)

print("⚡ GateSter Fine-Tuned LLM Server is Warm and READY on GPU!")

class GenerateRequest(BaseModel):
    prompt: str
    max_tokens: int = 512
    temperature: float = 0.1

@app.get("/health")
def health_check():
    return {"status": "online", "model": MODEL_ID}

@app.post("/generate")
def generate_text(req: GenerateRequest):
    try:
        messages = [
            {
                "role": "system",
                "content": "You are GateSter's Stage 0 Question Analyzer. Analyze raw GATE CS/IT questions and return ONLY a structured Stage 0 Blueprint JSON."
            },
            {
                "role": "user",
                "content": req.prompt
            }
        ]
        
        inputs = tokenizer.apply_chat_template(
            messages,
            tokenize=True,
            add_generation_prompt=True,
            return_tensors="pt"
        ).to("cuda")

        with torch.no_grad():
            outputs = model.generate(
                input_ids=inputs,
                max_new_tokens=req.max_tokens,
                temperature=req.temperature,
                do_sample=True if req.temperature > 0 else False,
                use_cache=True
            )
        
        # Decode response text
        response = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
        
        # Extract assistant response portion if ChatML system/user prompts are echoed
        if "assistant\n" in response:
            response = response.split("assistant\n")[-1]
        elif "assistant" in response:
            response = response.split("assistant")[-1]

        return {"response": response.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)