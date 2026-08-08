import os
import sys
import json
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List
from api_helper import safe_generate_json, UnifiedResponse
from retrieve_local import retrieve


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# from retrieve_local import retrieve

load_dotenv()

ai_client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

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
    print(f"Error: '{input_file}' not found! Run clean_deduplicate.py first")
    exit(1)

with open(input_file, "r", encoding = "utf-8") as f:
    raw_questions = json.load(f)

blueprints = {}
if os.path.exists(output_blueprint_file):
    with open(output_blueprint_file, "r", encoding = "utf-8") as f:
        blueprints = json.load(f)
    print(f"RESUMING! Already annoted {len(blueprints)} / {len(raw_questions)} questions")
print(f"Starting Safe RAG-Powered Stage 0 Annotation on {len(raw_questions)} questions...")
config = types.GenerateContentConfig(
    response_mime_type = "application/json",
    response_schema = Stage0Blueprint
)

for idx,q in enumerate(raw_questions):
    q_text = q.get("question_text", "").strip()
    year = q.get("year", 0)
    options = q.get("options", [])

    q_id = f"GATE_{year}_Q{idx+1}"
    if q_id in blueprints:
        continue
    retrieved_passages = []
    try:
        retrieved_passages = retrieve(q_text, top_k = 2)
        notes_context = "\n\n".join([f"GO Classes Note Chunk {i+1}:\n{p}" for i, p in enumerate(retrieved_passages)])
    except Exception as e:
        print(f"Qdrant retrieval warning for {q_id}: {e}")
        notes_context = "No specific note chunk retrieved."
    prompt = f"""
    Analyze this GATE CS/IT question. You MUST use the provided GO Classes Revision Notes from Qdrant to determine the `core_concept` and `requires_calculation` fields!
    ### GO CLASSES REVISION NOTES (FROM QDRANT VECTOR DB):
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
    """

    try:
        res = safe_generate_json(ai_client, "gemini-2.0-flash", prompt, config, llm = "gemini")
        metadata = json.loads(res.text)

        metadata["question_id"] = q_id
        metadata["year"] = year
        metadata["question"] = q_text
        metadata["options"] = options
        metadata["retrieved_go_classes_notes"] = retrieved_passages

        blueprints[q_id] = metadata

        print(f"[{idx+1}/{len(raw_questions)}] {q_id} | Subject: {metadata['subject']} | Concept: {metadata['core_concept']} | Type: {metadata['question_type']}")
    except Exception as e:
        print(f"Skipping {q_id} after retries: {e}")
    with open(output_blueprint_file, "w", encoding="utf-8") as f:
        json.dump(blueprints, f, indent = 2)
    with open(output_jsonl_file, "w", encoding = "utf-8") as f_jsonl:
        for b_id, b_data in blueprints.items():
            sample = {
                "messages": [
                    {
                        "role": "system",
                        "content": "You are GateSter's Stage 0 Question Analyzer. Analyze raw GATE CS/IT questions and return ONLY a structured Stage 0 Blueprint JSON."
                    },
                    {
                        "role": "user",
                        "content": f"Analyze this GATE question:\n\n{b_data['question']}"
                    },
                    {
                        "role": "assistant",
                        "content": json.dumps(b_data, indent=2)
                    }
                ]
            }
            f_jsonl.write(json.dumps(sample)+"\n")
    time.sleep(4.2)

print("\n" + "="*60)
print(f"🎉 SAFE STAGE 0 ANNOTATION COMPLETE!")
print(f"💾 BLUEPRINT DATASET (Dataset B) : {output_blueprint_file}")
print(f"🔥 UNSLOTH FINE-TUNING FILE     : {output_jsonl_file}")
print(f"✨ TOTAL ANNOTATED BLUEPRINTS   : {len(blueprints)}")
print("="*60 + "\n")
    
