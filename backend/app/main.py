from fastapi import FastAPI

app = FastAPI(
    title="Enterprise Knowledge Copilot",
    description="Enterprise RAG platform for secure organizational knowledge retrieval",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "application": "Enterprise Knowledge Copilot",
        "status": "running"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}