from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.chat import router as chat_router
from app.api.documents import router as documents_router


app = FastAPI(
    title="Enterprise Knowledge Copilot",
    description="Secure enterprise RAG API",
    version="0.1.0"
)


# Frontend origins allowed to access the API
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# API routes
app.include_router(chat_router)
app.include_router(documents_router)


@app.get("/")
def root():
    return {
        "application": "Enterprise Knowledge Copilot",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }