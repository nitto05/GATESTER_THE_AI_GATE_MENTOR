import time
from retrieve_local import retrieve
from local_llm_client import query_local_llm

def run_end_to_end_rag():
    print("=== GATESTER FULL END TO END RAG PIPELINE ===")

    test_queries = [
        "What is a deadlock in Operating System?",
        "Explain SQL Joins and Types",
        "Explain about syntax analysis and what type of grammars are used in it..."
        ]

    for idx, query in enumerate(test_queries):
        print(f"\n============================")
        print(f"Student Query {idx + 1}: '{query}'")
        print(f"\n============================")

        t0 = time.time()
        retrieved_chunks = retrieve(query, top_k = 2)
        t_retrieval = (time.time() - t0) * 1000

        print(f"Step 1: Retrieved {len(retrieved_chunks)} note passages in {t_retrieval:.2f}ms")

        context_text = "\n\n" .join ([f"Note {i+1}:\n{chunk}" for i, chunk in enumerate(retrieved_chunks)])

        rag_prompt = f"""
        You are GateSter's expert AI GATE CS/IT Mentor. Answer the student's question concisely using the provided GATE revision notes.

        --- GATE REVISION NOTES --- 
        {context_text}

        ---STUDENT'S QUESTION---
        {query}
        """ 

        t1 = time.time()
        answer = query_local_llm(rag_prompt, max_tokens  = 250)
        t_generation = (time.time()-t1) * 1000

        print(f"Step 2 : GENERATED ANSWER IN {t_generation:.2f} ms")
        print(f"Total end-to-end latency : {(t_retrieval + t_generation):.2f}ms\n")
        print("===GATESTER MENTOR ANSWER===")
        print(answer)

run_end_to_end_rag()