import os 
import uuid

from dotenv import load_dotenv

import google.generativeai as genai
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from langchain_text_splitters import MarkdownTextSplitter

load_dotenv()

genai.configure(api_key = os.getenv("GEMINI_API_KEY"))

client = QdrantClient(url = os.getenv("QDRANT_URL"),
api_key = os.getenv("QDRANT_API_KEY"))

with open("knowledge_base/books/revisionBook_cs_it.md", "r", encoding = "utf-8") as f:
    text = f.read()

splitter = MarkdownTextSplitter(chunk_size = 500, chunk_overlap = 50)
chunks = splitter.split_text(text)
print(f"Total chunks : {len(chunks)}")

if client.collection_exists("gate_books"):
    client.delete_collection("gate_books")
client.create_collection(collection_name = "gate_books", 
vectors_config = VectorParams(size = 768, distance = Distance.COSINE))

points = []

for i, chunk in enumerate(chunks):
    result = genai.embed_content(model = "models/text-embedding-004", content = chunk)

    points.append(PointStruct(
        id = str(uuid.uuid4()), 
        vector = result["embedding"],
        payload = {"text": chunk, "chunk_index" : i}
    ))

    if (i+1) %10 == 0:
        print(f"Embedded {i+1}/{len(chunks)} chunks...")
    
client.upsert(collection_name = "gate_books", points = points)
print(f"Done. Uploaded {len(points)} chunks to Qdrant. ")
