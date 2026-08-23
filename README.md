# Enterprise Knowledge Copilot

A local-first **Retrieval-Augmented Generation (RAG)** application for asking questions about enterprise documents.

Users can upload PDF documents, search them using semantic retrieval, and receive AI-generated answers grounded in the retrieved content with document and page citations.

## Features

- PDF upload and ingestion
- Semantic chunking
- Text embeddings
- PostgreSQL + pgvector
- Vector similarity search
- Cross-encoder reranking
- RAG prompt construction
- Local LLM with Ollama
- Qwen 2.5 3B
- Grounded answers with citations
- FastAPI REST API
- Next.js + TypeScript frontend
- Document list and deletion
- Chat History UI

## Architecture

```text
                    Enterprise Knowledge Copilot

                         Next.js Frontend
                               │
                               ▼
                          FastAPI API
                               │
              ┌────────────────┴────────────────┐
              │                                 │
        Document Upload                     User Question
              │                                 │
              ▼                                 ▼
         PDF Parsing                      Query Embedding
              │                                 │
              ▼                                 ▼
      Semantic Chunking                    pgvector
              │                                 │
              ▼                                 ▼
         Embeddings                       Top Passages
              │                                 │
              ▼                                 ▼
   PostgreSQL + pgvector                   Reranker
                                                │
                                                ▼
                                          RAG Prompt
                                                │
                                                ▼
                                        Ollama / Qwen
                                                │
                                                ▼
                                     Answer + Citations
```

## RAG Pipeline

```text
Question
   ↓
Embedding
   ↓
pgvector Search
   ↓
Top Candidate Passages
   ↓
Cross-Encoder Reranking
   ↓
Prompt Construction
   ↓
Qwen 2.5 3B
   ↓
Grounded Answer + Source
```

Example:

```text
Question:
How many hours can student employees work?

Answer:
Student employees may work a maximum of 20 hours per week
while classes are in session.

Source: employee_handbook.pdf, page 2
```

## Technology Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- pgvector
- Sentence Transformers
- Cross-Encoder reranking
- Ollama
- Qwen 2.5 3B

### Frontend
- Next.js
- React
- TypeScript
- Tailwind CSS

### Infrastructure
- Docker
- Docker Compose

## Project Structure

```text
enterprise-knowledge-copilot/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── generation/
│   │   ├── ingestion/
│   │   ├── models/
│   │   └── retrieval/
│   └── scripts/
│
├── frontend/
│   ├── app/
│   │   ├── documents/
│   │   └── history/
│   ├── components/
│   ├── services/
│   └── types/
│
├── data/
├── docker-compose.yml
└── README.md
```

## API Endpoints

```text
POST   /api/v1/ask
POST   /api/v1/documents/upload
GET    /api/v1/documents
DELETE /api/v1/documents/{id}
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

## Frontend

```text
/             Chat
/documents    Document Management
/history      Chat History
```

Development URL:

```text
http://localhost:3000
```

## Running the Project

### 1. Start PostgreSQL

```bash
docker compose up -d
```

### 2. Start Ollama

```bash
ollama serve
```

Make sure the model is available:

```bash
ollama pull qwen2.5:3b
```

### 3. Start Backend

```bash
cd backend
source venv/bin/activate
uvicorn app.main:app --reload
```

### 4. Start Frontend

```bash
cd frontend
npm run dev
```

Open:

```text
http://localhost:3000
```

## Testing

```bash
python -m scripts.test_search
python -m scripts.test_rerank
python -m scripts.test_llm
python -m scripts.test_rag
```

## Current Status

```text
PDF Upload                  ✓
Semantic Chunking           ✓
Embeddings                  ✓
pgvector Search             ✓
Cross-Encoder Reranking     ✓
Local LLM / Ollama          ✓
RAG Answer Generation       ✓
Source Citations            ✓
FastAPI API                 ✓
Next.js Frontend            ✓
Document Management         ✓
Chat History UI             ✓
Persistent Chat History     In Progress
```

## Goal

Enterprise Knowledge Copilot demonstrates an end-to-end **enterprise RAG system** combining document ingestion, embeddings, vector search, reranking, local LLM inference, grounded generation, REST APIs, and a full-stack web interface.