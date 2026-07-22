import os 
import uuid
from dotenv import load_dotenv
# from google import genai
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from langchain_text_splitters import MarkdownTextSplitter
from sentence_transformers import SentenceTransformer

load_dotenv()

# ai_client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

client = QdrantClient(
    url = os.getenv("QDRANT_URL"),
    api_key = os.getenv("QDRANT_API_KEY")
)

print("Loading local embedding model (BAAI/bge-small-en-v1.5)...")
embed_model = SentenceTransformer("BAAI/bge-small-en-v1.5")

with open("knowledge_base/books/revisionBook_cs_it.md", "r", encoding = "utf-8") as f:
    text = f.read()

splitter = MarkdownTextSplitter(chunk_size = 500, chunk_overlap = 50)
chunks = splitter.split_text(text)
print(f"Total chunks : {len(chunks)}")

if client.collection_exists("gate_books"):
    client.delete_collection("gate_books")

client.create_collection(
    collection_name = "gate_books",
    vectors_config = VectorParams(size=384, distance = Distance.COSINE)
)

print("Embedding chunks locally (0 cloud API calls)...")

embeddings = embed_model.encode(chunks, batch_size=64, show_progress_bar = True)

points = []
for i, vecotr in enumerate(embeddings):
    points.append(PointStruct(
        id = str(uuid.uuid4()),
        vector = vecotr.tolist(),
        payload = {"text": chunks[i], "chunk_index" : i}
    ))

upload_batch_size = 250
for i in range(0, len(points), upload_batch_size):
    batch_points = points[i: i+ upload_batch_size]
    client.upsert(collection_name = "gate_books", points=batch_points)
    print(f"Uploaded batch {i // upload_batch_size + 1}/{(len(points)+upload_batch_size-1) // upload_batch_size} to Qdrant Cloud...")
print(f"Done. Uploaded{len(points)} chunks to Qdrant!!!!")
