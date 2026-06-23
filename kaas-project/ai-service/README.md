# KaaS AI Service

## Overview
This repository contains the **KaaS AI Service**, a FastAPI backend that powers an AI‑driven learning platform. It includes:
- Structured data ingestion (CSV datasets) and unstructured knowledge (PDFs, videos, notes).
- A **Recommendation Engine**, **Assessment AI**, **Predictive ML**, and **Analytics** built on top of the structured data.
- A **RAG AI Tutor** that performs context‑aware answering, course explanations, and knowledge retrieval using Large Language Models (Groq Llama‑3.1‑8b‑instant).

---

### KaaS AI Data Architecture
```
KaaS AI Data Architecture
                    KaaS AI SERVICE

                           |
        ----------------------------------------
        |                                      |
        ↓                                      ↓

 Structured Data                     Unstructured Knowledge

 CSV / Database                      PDFs / Videos / Notes

        |                                      |
        ↓                                      ↓

 Recommendation Engine               RAG AI Tutor

 Assessment AI                        Course Explanation

 Predictive ML                        Context Answering

 Analytics                            Knowledge Retrieval
```
---

The service is organized as follows:
```
kaas-project/
├─ frontend/          # (existing frontend)
├─ backend/           # (existing backend)
└─ ai-service/        # (this service)
   ├─ app/
   │   ├─ main.py
   │   ├─ config/settings.py
   │   ├─ api/routes.py
   │   ├─ llm/ (Groq client and prompt)
   │   ├─ rag/ (loader, splitter, embeddings, vector_store, retriever)
   │   └─ ...
   ├─ data/
   │   ├─ documents/   # unstructured files (PDFs, etc.)
   │   └─ datasets/    # CSV datasets listed in the README description
   └─ requirements.txt
```

You can now start the service with:
```bash
uvicorn app.main:app --reload --port 8001
```

Feel free to explore the automatically generated Swagger UI at `http://127.0.0.1:8001/docs`.
