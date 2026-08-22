from fastapi import FastAPI

from app.api.chat import router as chat_router


app = FastAPI(
    title="Enterprise Knowledge Copilot",
    description="Secure enterprise RAG API",
    version="0.1.0"
)


app.include_router(chat_router)


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