import os 
import uuid
from dotenv import load_dotenv
from google import genai
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from langchain_text_splitters import MarkdownTextSplitter

load_dotenv()

ai_client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

client = QdrantClient(
    url = os.getenv("QDRANT_URL"),
    api_key = os.getenv("QDRANT_API_KEY")
)

with open("knowledge_base/books/revisionBook_cs_it.md", "r", encoding = "utf-8") as f:
    text = f.read()

splitter = MarkdownTextSplitter(chunk_size = 500, chunk_overlap = 50)
chunks = splitter.split_text(text)
print(f"Total chunks : {len(chunks)}")

if client.collection_exists("gate_books"):
    client.delete_collection("gate_books")

client.create_collection(
    collection_name = "gate_books",
    vectors_config = VectorParams(size=3072, distance = Distance.COSINE)
)

points = []
batch_size = 100

for i in range(0, len(chunks), batch_size):
    batch_chunks = chunks[i : i+batch_size]

    response = ai_client.models.embed_content(
        model = "gemini-embedding-2",
        contents = batch_chunks
    )

    for j, embedding_obj in enumerate(response.embeddings):
        chunk_index = i+j
        points.append(PointStruct(
            id = str(uuid.uuid4()),
            vector = embedding_obj.values,
            payload = {"text" : batch_chunks[j], "chunks_index" : chunk_index}
        ))

    print(f"Embedded batch {i // batch_size + 1}: chunks {i} to {min(i + batch_size, len(chunks))}... ")

client.upsert(collection_name = "gate_books", points=points)
print(f"Done. Uploaded{len(points)} chunks to Qdrant.")
