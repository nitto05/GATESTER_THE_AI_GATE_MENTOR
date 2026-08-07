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

ai_client = genai.client(api_key = os.getenv("GEMINI_API_KEY"))

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
    