import json
import os
import re

# Strict Keyword Taxonomy Mapping Rules for GATE CS
SUBJECT_KEYWORD_RULES = {
    "Theory of Computation": [
        "automata", "dfa", "nfa", "regular expression", "cfg", "context free",
        "pumping lemma", "turing machine", "pda", "pushdown", "grammar",
        "undecidable", "decidable", "chomsky", "alphabet", "regular language"
    ],
    "Databases (DBMS)": [
        "acid", "sql", "relational", "functional dependency", "normalization",
        "b+ tree", "b-tree", "transaction", "concurrency", "locking", "2pl",
        "serializability", "er diagram", "foreign key", "primary key", "tuple calculus", "relational algebra"
    ],
    "Data Structures": [
        "linked list", "binary tree", "stack", "queue", "heap", "bst",
        "binary search tree", "array", "pointer", "struct", "node", "hash table",
        "traversal", "inorder", "preorder", "postorder", "avl tree"
    ],
    "Algorithms": [
        "dijkstra", "knapsack", "dynamic programming", "greedy", "sorting",
        "quicksort", "mergesort", "asymptotic", "big-o", "recurrence", "master theorem",
        "divide and conquer", "bfs", "dfs", "minimum spanning tree", "kruskal", "prim"
    ],
    "Operating Systems": [
        "deadlock", "paging", "virtual memory", "semaphore", "process", "thread",
        "cpu scheduling", "round robin", "fcfs", "sjf", "banker's algorithm", "page fault",
        "fifo", "lru", "belady", "synchronization", "mutex", "fork"
    ],
    "Computer Organization and Architecture": [
        "pipelining", "cache", "addressing mode", "alu", "instruction", "hazard",
        "microprogramming", "direct mapping", "set associative", "dma", "interrupt",
        "registers", "clock cycle", "cpi"
    ],
    "Computer Networks": [
        "tcp", "ip", "udp", "subnetting", "router", "switch", "mac address",
        "osi", "layer", "http", "dns", "sliding window", "go-back-n", "selective repeat",
        "flow control", "congestion", "ip addressing", "ipv4", "ipv6"
    ],
    "Digital Logic": [
        "multiplexer", "mux", "decoder", "boolean", "k-map", "karnaugh",
        "flip flop", "counter", "adder", "combinational", "sequential", "logic gate",
        "2's complement", "floating point", "ieee 754"
    ],
    "Compiler Design": [
        "parsing", "parser", "lexical", "lexer", "slr", "clr", "lalr", "ll(1)",
        "syntax directed", "sdt", "intermediate code", "three address code", "code optimization",
        "basic block", "dag"
    ],
    "Discrete Mathematics": [
        "propositional", "first order logic", "lattice", "group", "graph theory",
        "relation", "partial order", "poset", "combinatorics", "permutation", "combination",
        "planarity", "chromatic", "isomorphism"
    ],
    "Engineering Mathematics": [
        "eigenvalue", "eigenvector", "matrix", "determinant", "probability",
        "bayes", "poisson", "normal distribution", "calculus", "limit", "derivative", "integration"
    ],
    "General Aptitude": [
        "verbal", "numerical", "spatial", "contour", "pattern", "geometry", "analogy"
    ]
}

blueprint_file = "data/dataset_b_blueprint.json"
output_jsonl_file = "data/stage0_finetune_dataset.jsonl"

if not os.path.exists(blueprint_file):
    print(f"❌ Error: '{blueprint_file}' not found!")
    exit(1)

with open(blueprint_file, "r", encoding="utf-8") as f:
    blueprints = json.load(f)

total = len(blueprints)
correct_matches = 0
corrected_count = 0
reclassified_log = []

for q_id, b in blueprints.items():
    current_subject = b.get("subject", "").strip()
    q_text = (b.get("question", "") + " " + b.get("topic", "") + " " + b.get("core_concept", "")).lower()

    # Find matching subject based on keyword occurrence
    matched_subject = None
    max_keyword_hits = 0

    for subject, keywords in SUBJECT_KEYWORD_RULES.items():
        hits = sum(1 for kw in keywords if re.search(r'\b' + re.escape(kw) + r'\b', q_text))
        if hits > max_keyword_hits:
            max_keyword_hits = hits
            matched_subject = subject

    # Check alignment
    if matched_subject and matched_subject != current_subject and max_keyword_hits >= 1:
        corrected_count += 1
        reclassified_log.append(f"  🔧 [{q_id}] Reclassified: '{current_subject}' ➔ '{matched_subject}' (Keyword hits: {max_keyword_hits})")
        b["subject"] = matched_subject
    else:
        correct_matches += 1

print("=" * 68)
print("       🔍 GATESTER TAXONOMY KEYWORD VERIFICATION REPORT           ")
print("=" * 68)
print(f"📊 Total Blueprints Audited       : {total}")
print(f"✅ Perfectly Matched Subjects    : {correct_matches} ({correct_matches/total*100:.1f}%)")
print(f"🔧 Auto-Corrected Misplacements   : {corrected_count} ({corrected_count/total*100:.1f}%)")
print("-" * 68)

if len(reclassified_log) > 0:
    print("\nRECLASSIFICATION HIGHLIGHTS (Top 10):")
    for log_entry in reclassified_log[:10]:
        print(log_entry)

# Save verified blueprints back to disk
with open(blueprint_file, "w", encoding="utf-8") as f:
    json.dump(blueprints, f, indent=2)

# Update jsonl fine-tuning dataset
with open(output_jsonl_file, "w", encoding="utf-8") as f_jsonl:
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
        f_jsonl.write(json.dumps(sample) + "\n")

print("\n" + "=" * 68)
print("🎉 TAXONOMY VERIFICATION & AUTO-CORRECTION COMPLETE!")
print(f"💾 VERIFIED BLUEPRINTS SAVED TO : {blueprint_file}")
print(f"🔥 VERIFIED UNSLOTH FILE SAVED TO: {output_jsonl_file}")
print("=" * 68 + "\n")
