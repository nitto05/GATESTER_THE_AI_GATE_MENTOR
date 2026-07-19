import os
from dotenv import load_dotenv
from google import genai  # #############
from qdrant_client import QdrantClient

load_dotenv()

ai_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))  # #############

client = QdrantClient(
        url =os.getenv("QDRANT_URL"),
        api_key = os.getenv("QDRANT_API_KEY") 
    )

def retrieve (query: str, top_k: int = 5):
    """
        Embeds the user query and searches the 'gate_books' collection
        in Qdrant for the top_k most semantically similar chunks.
    """

    response = ai_client.models.embed_content(              # #############
            model = "gemini-embedding-2",                   # #############
            contents = query                                # #############
    )                                                       # #############
    query_vector = response.embeddings[0].values            # #############

    response = client.query_points(
        collection_name = "gate_books",
        query = query_vector,
        limit = top_k
    )
    hits = response.points

    return [hit.payload["text"] for hit in hits]
    
# if __name__ == "__main__":
#     test_query = "What is a deadlock?"
#     print(f"Searching Qdrant for: '{test_query}'...\n")
    
#     try:
#         matched_chunks = retrieve(test_query, top_k=3)
#         for idx, text in enumerate(matched_chunks):
#             print(f"── Match {idx + 1} ──")
#             print(text)
#             print("-" * 50)
#     except Exception as e:
#         print(f"An error occurred during retrieval: {e}")