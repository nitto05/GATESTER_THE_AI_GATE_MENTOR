import os 
from qdrant_client import QdrantClient
from retrieve import retrieve

def run_diagnostics():
    print("=== STARTING GATESTER RAG PIPELINE TEST ===")

    qdrant_url = os.getenv("QDRANT_URL")
    qdrant_key = os.getenv("QDRANT_API_KEY")

    if not qdrant_url or not qdrant_key:
        print(" Error : Missing Qdrant environment variables in .env file.")
        return

    print("Checking connection to Qdrant Cloud...")

    client = QdrantClient(url = qdrant_url, api_key = qdrant_key)
    try:
        exists = client.collection_exists("gate_books")
        if exists :
            info = client.get_collection("gate_books")
            print(f" connected! collection 'gate_books' exists with {info.points_count} chunks.")
        else:
            print(f"collection 'gate_books' does not exist yet. You must run ingest.py first!")
            return
    except Exception as e:
        print(f"Failed to connect to Qdrant : {e}")
        return
    test_queries = ["What is a deadlock in Operating Systems?", "Explain SQL Joins and types", "Explain packet switching vs circuit switching"]

    for idx, query in enumerate(test_queries):
        print(f"\nTest Query {idx + 1} : '{query}'")
        print("retrieving marchign contents...")
        try:
            results = retrieve(query, top_k = 2)
            if not results : 
                print("No matches found.")
            for hit_idx, text in enumerate(results):
                print(f"\n [Match {hit_idx +1}]")
                preview = text.strip().replace('\n', ' ')[:250]
                print(f"{preview}...")
        except Exception as e:
            print(f"Query failed : {e}")

run_diagnostics()