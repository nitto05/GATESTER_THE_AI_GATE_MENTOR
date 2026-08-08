import os
import sys
import json
import time
import re
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field
from typing import List

# Import API Helper & Qdrant Retriever
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from api_helper import safe_generate_json, UnifiedResponse
from retrieve_local import retrieve

load_dotenv()

ai_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

GATE_SYLLABUS_TAXONOMY = """
OFFICIAL GATE CS/IT SUBJECTS & TOPICS:
1. Engineering Mathematics: Linear Algebra, Calculus, Probability & Statistics.
2. Discrete Mathematics: Propositional & First Order Logic, Sets, Relations, Functions, Partial Orders, Lattices, Groups, Graph Theory, Combinatorics.
3. Digital Logic: Boolean Algebra, Combinational Circuits, Sequential Circuits, Minimization, Number Representations & Computer Arithmetic.
4. Computer Organization and Architecture: Machine Instructions & Addressing Modes, ALU, Data-Path & Control Unit, Instruction Pipelining, Pipeline Hazards, Memory Hierarchy (Cache, Main Memory, Virtual Memory), I/O Interface.
5. Data Structures: Arrays, Stacks, Queues, Linked Lists, Trees, Binary Search Trees, Binary Heaps, Graphs.
6. Algorithms: Searching, Sorting, Hashing, Asymptotic Analysis, Recurrences, Greedy Algorithms, Dynamic Programming, Divide-and-Conquer, Graph Traversals, Shortest Paths, Minimum Spanning Trees.
7. Theory of Computation: Regular Expressions, Finite Automata (DFA/NFA), Context-Free Grammars, Pushdown Automata, Pumping Lemma, Turing Machines, Undecidability.
8. Compiler Design: Lexical Analysis, Parsing (LL/LR/LALR), Syntax Directed Translation, Runtime Environments, Intermediate Code Generation, Code Optimization.
9. Operating Systems: Processes, Threads, CPU Scheduling, Inter-Process Communication, Concurrency & Synchronization, Semaphores, Deadlocks, Memory Management, Paging, Virtual Memory, File Systems, Disk Scheduling.
10. Databases (DBMS): ER-Model, Relational Model, Relational Algebra, Tuple Calculus, SQL, Normalization (1NF, 2NF, 3NF, BCNF), Transactions, Concurrency Control, Indexing (B/B+ Trees).
11. Computer Networks: Concept of Layering, OSI & TCP/IP Stacks, Flow & Error Control, Data Link Layer, IP Addressing, Subnetting, Routing Algorithms, IPv4/IPv6, TCP/UDP, Application Layer (DNS, HTTP, SMTP).
12. General Aptitude: Verbal Aptitude, Quantitative Aptitude, Analytical Aptitude, Spatial Aptitude.
"""

# Pydantic Schema for Stage 0 Metadata
class Stage0Blueprint(BaseModel):
    subject: str = Field(..., description="Must be one of the 12 official GATE CS subjects listed in taxonomy.")
    topic: str = Field(..., description="Specific sub-topic from the GATE CS syllabus.")
    core_concept: str = Field(..., description="STRICTLY extract from the provided GO Classes notes (e.g. Banker's Algorithm, Page Table Size Calculation, LR(0) Parsing).")
    question_type: str = Field(..., description="MCQ (Exactly 1 option correct), MSQ (1 or more options correct), or NAT (Numerical Answer Type - only a number).")
    requires_calculation: bool = Field(..., description="True if answering requires evaluating a mathematical formula or calculation found in GO Classes notes; False if pure theoretical concept.")
    mutable_fields: List[str] = Field(..., description="List of specific numbers or variable names that can be mutated, e.g. ['page_size', 'virtual_address_bits'].")
    immutable_fields: List[str] = Field(..., description="Structural rules or kernel assumptions that must NOT change, e.g. ['single_level_paging'].")
    transformation_rules: List[str] = Field(..., description="Allowed transformations: CHANGE_NUMBERS, CHANGE_OPTION_ORDER, CHANGE_VARIABLE_NAMES, REWORD_SENTENCE.")

input_file = "data/raw_pyqs_clean.json"
output_blueprint_file = "data/dataset_b_blueprint.json"
output_jsonl_file = "data/stage0_finetune_dataset.jsonl"

if not os.path.exists(input_file):
    print(f"❌ Error: '{input_file}' not found! Run clean_deduplicate.py first.")
    exit(1)

with open(input_file, "r", encoding="utf-8") as f:
    raw_questions = json.load(f)

# 🔄 AUTO-RESUME CHECK: Loads existing blueprints from laptop disk!
blueprints = {}
if os.path.exists(output_blueprint_file):
    with open(output_blueprint_file, "r", encoding="utf-8") as f:
        blueprints = json.load(f)
    print("\n" + "="*60)
    print(f"🔄 RESUMING! Already annotated {len(blueprints)} / {len(raw_questions)} questions on disk.")
    print("="*60 + "\n")

print(f"🚀 Starting RAG-Powered Stage 0 Annotation on {len(raw_questions)} questions using Kaggle Qwen GPU Server...")

class ConfigMock:
    def __init__(self, temp: float, max_tok: int):
        self.temperature = temp
        self.max_output_tokens = max_tok

config = ConfigMock(0.1, 1024)

for idx, q in enumerate(raw_questions):
    q_text = q.get("question_text", "").strip()
    year = q.get("year", 0)
    options = q.get("options", [])

    q_id = f"GATE_{year}_Q{idx+1}"
    
    # 🛑 SKIP ALREADY ANNOTATED QUESTIONS (Resumes instantly!)
    if q_id in blueprints:
        continue

    retrieved_passages = []
    try:
        retrieved_passages = retrieve(q_text, top_k=2)
        notes_context = "\n\n".join([f"GO Classes Note Chunk {i+1}:\n{p}" for i, p in enumerate(retrieved_passages)])
    except Exception as e:
        print(f"  ⚠️ Qdrant retrieval warning for {q_id}: {e}")
        notes_context = "No specific note chunk retrieved."

    prompt = f"""
    You are GateSter's Stage 0 Question Analyzer. Analyze this GATE CS/IT question using the provided GO Classes Revision Notes from Qdrant and return ONLY a valid JSON object.

    ### GO CLASSES REVISION NOTES:
    {notes_context}

    ### OFFICIAL GATE SYLLABUS TAXONOMY:
    {GATE_SYLLABUS_TAXONOMY}

    STRICT ANNOTATION RULES:
    1. CORE CONCEPT: Extract `core_concept` STRICTLY from the GO Classes Revision Notes provided above.
    2. CALCULATION LOGIC: Set `requires_calculation: true` if the GO Classes Notes show a mathematical formula or numerical step for this topic; else `false`.
    3. SUBJECT & TOPIC: Must match the official GATE CS taxonomy.
    4. QUESTION TYPE: MCQ (1 right option), MSQ (1+ right options), or NAT (Numerical Answer Type - no options).

    QUESTION STATEMENT:
    {q_text}
    
    OPTIONS:
    {json.dumps(options)}

    RETURN ONLY A VALID JSON OBJECT WITH EXACTLY THESE KEYS (No Markdown, No Extra Text):
    {{
      "subject": "Official GATE CS subject name",
      "topic": "Specific sub-topic",
      "core_concept": "Core concept extracted strictly from notes",
      "question_type": "MCQ",
      "requires_calculation": true,
      "mutable_fields": ["variable_name_or_number"],
      "immutable_fields": ["kernel_assumption"],
      "transformation_rules": ["CHANGE_NUMBERS", "CHANGE_OPTION_ORDER"]
    }}
    """

    try:
        # 🚀 Sends HTTP request to Kaggle Warm GPU LLM Server via safe_generate_json
        res = safe_generate_json(ai_client, "qwen-2.5-3b", prompt, config, llm="qwen")
        
        response_text = res.text.strip()
        match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if match:
            parsed_raw = json.loads(match.group(0))
        else:
            parsed_raw = json.loads(response_text)

        # 🛡️ PYDANTIC SCHEMA VALIDATION!
        validated_blueprint = Stage0Blueprint.model_validate(parsed_raw)
        metadata = validated_blueprint.model_dump()

        metadata["question_id"] = q_id
        metadata["year"] = year
        metadata["question"] = q_text
        metadata["options"] = options
        metadata["retrieved_go_classes_notes"] = retrieved_passages

        blueprints[q_id] = metadata

        print(f"  ✅ [{idx+1}/{len(raw_questions)}] {q_id} | Subject: {metadata.get('subject')} | Concept: {metadata.get('core_concept')}")

        # 🔍 LIVE INSPECTION SAMPLE (1st question immediately, then every 20th question!)
        if len(blueprints) == 1 or len(blueprints) % 20 == 0:
            print("\n" + "🔍 " + "="*58)
            print(f"   LIVE INSPECTION SAMPLE (Question #{len(blueprints)}: {q_id})")
            print("="*60)
            print(f"   📌 Subject              : {metadata.get('subject')}")
            print(f"   📌 Topic                : {metadata.get('topic')}")
            print(f"   📌 Core Concept         : {metadata.get('core_concept')}")
            print(f"   📌 Question Type        : {metadata.get('question_type')}")
            print(f"   📌 Requires Calculation : {metadata.get('requires_calculation')}")
            print(f"   📌 Mutable Fields       : {metadata.get('mutable_fields')}")
            print(f"   📌 Immutable Fields     : {metadata.get('immutable_fields')}")
            print(f"   📌 Transformation Rules : {metadata.get('transformation_rules')}")
            print("="*60 + "\n")

        # Fast append single line to .jsonl
        sample = {
            "messages": [
                {
                    "role": "system",
                    "content": "You are GateSter's Stage 0 Question Analyzer. Analyze raw GATE CS/IT questions and return ONLY a structured Stage 0 Blueprint JSON."
                },
                {
                    "role": "user",
                    "content": f"Analyze this GATE question:\n\n{metadata['question']}"
                },
                {
                    "role": "assistant",
                    "content": json.dumps(metadata, indent=2)
                }
            ]
        }
        with open(output_jsonl_file, "a", encoding="utf-8") as f_jsonl:
            f_jsonl.write(json.dumps(sample) + "\n")

    except Exception as e:
        print(f"  ❌ Skipping {q_id} after retries: {e}")

    # Auto-save master dictionary to disk every 20 questions
    if (idx + 1) % 20 == 0 or (idx + 1) == len(raw_questions):
        with open(output_blueprint_file, "w", encoding="utf-8") as f:
            json.dump(blueprints, f, indent=2)

    time.sleep(0.2)  # High-speed local loop pacing

print("\n" + "="*60)
print(f"🎉 STAGE 0 ANNOTATION COMPLETE (POWERED BY KAGGLE QWEN GPU)!")
print(f"💾 BLUEPRINT DATASET (Dataset B) : {output_blueprint_file}")
print(f"🔥 UNSLOTH FINE-TUNING FILE     : {output_jsonl_file}")
print(f"✨ TOTAL ANNOTATED BLUEPRINTS   : {len(blueprints)}")
print("="*60 + "\n")
