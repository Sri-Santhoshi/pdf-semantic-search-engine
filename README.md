# PDF Semantic Search Engine

## 📌 Overview

This project implements a semantic search system for PDF documents using vector embeddings. Instead of traditional keyword matching, it retrieves results based on meaning and context.

---

## 🚀 Features

* Extracts text from PDF documents
* Splits text into meaningful chunks
* Converts text into vector embeddings
* Stores embeddings using FAISS
* Retrieves relevant content using semantic similarity
* FastAPI-based query endpoint

---

## 🛠️ Tech Stack

* Python
* PyMuPDF (PDF text extraction)
* Sentence Transformers (MiniLM)
* FAISS (Vector Database)
* FastAPI (API development)

---

## ⚙️ How It Works

### 1. Ingestion Pipeline

* Reads PDF file
* Splits text into chunks (300 words with 50 overlap)
* Generates embeddings for each chunk
* Stores embeddings in FAISS index

### 2. Retrieval System

* Accepts user query via API
* Converts query into embedding
* Performs similarity search
* Returns top relevant chunks with page numbers

---

## ▶️ How to Run

### Step 1: Install dependencies

pip install pymupdf sentence-transformers faiss-cpu fastapi uvicorn

### Step 2: Run ingestion

python ingest.py

### Step 3: Start API

uvicorn app:app --reload

### Step 4: Test API

Open: http://127.0.0.1:8000/docs

---

## 📄 Example Query

```json
{
  "query": "What is this document about?",
  "top_k": 3
}
```

---

## 📊 Output

Returns:

* Relevant text chunks
* Page numbers
* Similarity scores

---

## 🧠 Design Choices

* Chunk Size: 300 (balanced context and performance)
* Overlap: 50 (maintains continuity)
* Model: MiniLM (fast and efficient)
* Vector DB: FAISS (high-speed similarity search)

---

## 📌 Note

vector.index and metadata.pkl are generated files and can be recreated by running ingest.py.

---

## 🔮 Future Improvements

* Add UI for better interaction
* Improve ranking of results
* Support multiple documents
