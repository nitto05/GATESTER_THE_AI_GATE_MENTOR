import os
import uuid
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Try PyMuPDF (fitz) or pypdf
try:
    import fitz
    USE_FITZ = True
except ImportError:
    import pypdf
    USE_FITZ = False

load_dotenv()

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)

print("Loading local embedding model (BAAI/bge-small-en-v1.5)...")
embed_model = SentenceTransformer("BAAI/bge-small-en-v1.5")

# GO Classes Notes PDF paths
files_to_ingest = [
    ("knowledge_base/books/go_classes_notes_1.pdf", "pdf"),
    ("knowledge_base/books/go_classes_notes_2.pdf", "pdf")
]

all_chunks = []
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

for file_path, file_type in files_to_ingest:
    if os.path.exists(file_path):
        print(f"📖 Ingesting '{file_path}'...")
        full_text = ""
        if file_type == "pdf":
            if USE_FITZ:
                doc = fitz.open(file_path)
                for page in doc:
                    full_text += page.get_text() + "\n"
                doc.close()
            else:
                reader = pypdf.PdfReader(file_path)
                for page in reader.pages:
                    full_text += (page.extract_text() or "") + "\n"
        elif file_type == "md":
            with open(file_path, "r", encoding="utf-8") as f:
                full_text = f.read()

        chunks = text_splitter.split_text(full_text)
        print(f"   Created {len(chunks)} text chunks from {file_path}.")
        all_chunks.extend(chunks)
    else:
        print(f"  ⚠️ Warning: '{file_path}' not found!")

print(f"\n📚 Total Combined Chunks across all notes: {len(all_chunks)}")

# Re-create gate_books collection in Qdrant Cloud
if client.collection_exists("gate_books"):
    client.delete_collection("gate_books")

client.create_collection(
    collection_name="gate_books",
    vectors_config=VectorParams(size=384, distance=Distance.COSINE)
)

print("\n⚡ Embedding all GO Classes notes locally & uploading to Qdrant Cloud...")

embeddings = embed_model.encode(all_chunks, batch_size=64, show_progress_bar=True)

points = []
for i, vector in enumerate(embeddings):
    points.append(PointStruct(
        id=str(uuid.uuid4()),
        vector=vector.tolist(),
        payload={"text": all_chunks[i], "chunk_index": i}
    ))

upload_batch_size = 250
for i in range(0, len(points), upload_batch_size):
    batch_points = points[i:i + upload_batch_size]
    client.upsert(collection_name="gate_books", points=batch_points)
    print(f"   Uploaded batch {i // upload_batch_size + 1}/{(len(points)+upload_batch_size-1) // upload_batch_size} to Qdrant Cloud...")

print(f"\n🎉 DONE! Uploaded {len(points)} GO Classes Notes chunks to Qdrant Cloud 'gate_books' collection!")
