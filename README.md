# AI Text Intelligence API 🚀

**FastAPI-based backend** for **sentiment analysis**, **text summarization**, **semantic text ingestion**, and **Retrieval-Augmented Generation (RAG)** using a **local Large Language Model**.

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-brightgreen.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-ready-blue.svg)](https://www.docker.com/)

## Features

- 🔍 **Plain text ingestion** for semantic indexing
- 🗄️ **Vector storage** using ChromaDB
- 🤗 **HuggingFace sentence-transformer embeddings**
- 🎯 **Source-aware RAG** to prevent hallucination
- 🧠 **Local LLM inference** using Ollama (Gemma 2B)
- ⚠️ **Graceful degradation** when LLM unavailable
- 🏗️ **Clean service-based architecture**
- 💾 **Persistent vector database**
- 🐳 **Docker-ready deployment**

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| **Framework** | Python 3.11, FastAPI |
| **Embeddings** | HuggingFace Sentence Transformers |
| **Vector DB** | ChromaDB |
| **LLM** | Ollama (Gemma 2B) |
| **Runtime** | ONNX Runtime (pinned) |
| **Orchestration** | LangChain |
| **Container** | Docker |

## 🚀 Quick Start

### 1. Install & Setup Ollama
```
Download from https://ollama.com/

ollama pull gemma:2b<br>
```

### 2. Clone & Setup
```
git clone https://github.com/Om-128/ai-text-intelligence-api.git

cd ai-text-intelligence-api
``` 
### 3. Virtual Environment
```
python -m venv test_env

Activate On Windows:
test_env\Scripts\activate

Activate On Linux/Mac:
source test_env/bin/activate

```

### 4. Install Dependencies
```
pip install -r requirements.txt
```

### 5. Run the FastAPI
```
python -m uvicorn app.main:app --reload
```

### 6. API Usage

```
Text Analysis
  - POST /analyze <br>
  - add Content-Type: json

Text Summarization
  - POST /summarize <br>
  - add Content-Type: text/plain

Semantic Text Ingestion
  - POST /semantic_add/ <br>
  - add Content-Type: text/plain

Semantic RAG Query
  - POST /semantic_search/ <br>
  - add Content-Type: text/plain
```

### 🐳 Docker Support
### Build
docker build -t ai-text-intelligence-api .

### Run (Ollama must be running on host)
docker run -p 8000:8000 ai-text-intelligence-api


### 📁 Project Structure
text
```
ai-text-intelligence-api/
├── app/
│   ├── api/
│   │   └── analyze.py         # Sentiment analysis and keywords API
│   │   └── summarize.py       # Text summarization API
│   │   ├── semantic_add.py    # Ingestion API
│   │   └── semantic_rag.py    # RAG API
│   ├── services/
│   │   └── semantic_search/
│   │       ├── embeddings.py     # Embedding model
│   │       ├── ingest.py         # Ingestion logic
│   │       └── rag.py            # RAG logic
│   │   └── sentiment_service.py  # Sentiment analysis
│   │   └── keyword_service.py    # Top keywords logic
│   │   └── summarization_service # Text summarization logic
│   ├── utils.py
│   ├── CustomException.py
│   └── main.py
├── vectorstore/
│   └── chroma_db/             # Persistent storage
├── requirements.txt
├── Dockerfile
└── README.md
```

🔍 Notes <br>
#### Automatic DB Creation: Vector database and collections created on first use

#### LLM Fallback: Semantic retrieval works even if Ollama unavailable

#### Local Only: Designed for experimentation and evaluation

#### Pinned Dependencies: All native libraries version-locked for stability