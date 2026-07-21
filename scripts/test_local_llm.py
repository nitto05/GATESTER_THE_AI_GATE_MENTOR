import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer

model_id = "unsloth/Qwen3-4B-Instruct-2507-unsloth-bnb-4bit"

print("Loading model...")
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="cuda:0", torch_dtype = torch.float16)

streamer = TextStreamer(tokenizer, skip_prompt = True)

print("Generating response...\n")
prompt = "Hi! what is the capital of india??, give the description of the capital in 100 words only. do not exceed the word limit and try not to make any gramatical errors.\n\n"

inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
# output = model.generate(**inputs, max_new_tokens = 300)
print("=== OUTPUT ===")
# print(tokenizer.decode(output[0], skip_special_tokens = True))
output = model.generate(**inputs, streamer = streamer, max_new_tokens = 1024)