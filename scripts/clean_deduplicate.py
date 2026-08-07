import json
import os

raw_path = "data/raw_pyqs.json"
clean_path = "data/raw_pyqs_clean.json"

if not os.path.exists (raw_path):
    print(f" Error: '{raw_path}' not found! Please place your raw_Pyqs.json in the 'data' folder")
else:
    print(f"Reading '{raw_path}'...")
    with open(raw_path, "r", encoding = "utf-8") as f:
        raw_questions = json.load(f)
    print(f"Deduplicating {len(raw_questions)} question records...")

    unique_dict = {}
    for q in raw_questions:
        text = q.get("question_text", "").strip()
        if text and text not in unique_dict:
            unique_dict[text] = q
    unique_questions = list(unique_dict.values())

    with open(clean_path, "w", encoding = "utf-8") as f:
        json.dump(unique_questions, f, indent = 2)
    print("\n" + "="*60)
    print(f"RAE EXTRACTED RECORDS : {len(raw_questions)}")
    print(f"UNIQUE MASTER QUESTIONS : {len(unique_questions)}")
    print(f"SAVED TO : {clean_path}")
    print("="*60 + "\n")