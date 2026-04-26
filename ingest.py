import fitz
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Step 1: Read PDF
def read_pdf(file):
    doc = fitz.open(file)
    data = []
    for i, page in enumerate(doc):
        text = page.get_text()
        data.append((i+1, text))
    return data

# Step 2: Chunk text
def chunk_text(text, chunk_size=300, overlap=50):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)

    return chunks

# Step 3 + 4: Process and store
def main():
    pdf_data = read_pdf("sample.pdf")

    all_chunks = []
    metadata = []

    for page_num, text in pdf_data:
        chunks = chunk_text(text)

        for chunk in chunks:
            all_chunks.append(chunk)
            metadata.append((chunk, page_num))

    # Convert to embeddings
    embeddings = model.encode(all_chunks)

    # Store in FAISS
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    # Save files
    faiss.write_index(index, "vector.index")

    with open("metadata.pkl", "wb") as f:
        pickle.dump(metadata, f)

    print("Ingestion complete!")

if __name__ == "__main__":
    main()