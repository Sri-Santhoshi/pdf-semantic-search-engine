from fastapi import FastAPI
from pydantic import BaseModel
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

app = FastAPI()

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load vector DB
index = faiss.read_index("vector.index")

# Load metadata
with open("metadata.pkl", "rb") as f:
    metadata = pickle.load(f)

# Request format
class Query(BaseModel):
    query: str
    top_k: int = 3

# API endpoint
@app.post("/query")
def search(q: Query):
    query_embedding = model.encode([q.query])

    D, I = index.search(np.array(query_embedding), q.top_k)

    results = []

    for i, idx in enumerate(I[0]):
        chunk, page = metadata[idx]

        results.append({
            "chunk_text": chunk,
            "page_number": page,
            "score": float(D[0][i])
        })

    return results