from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.generation.rag_service import ask_question


router = APIRouter(
    prefix="/api/v1",
    tags=["chat"]
)


class AskRequest(BaseModel):
    question: str
    conversation_id: int | None = None


class SourceResponse(BaseModel):
    document: str
    page: int
    chunk_index: int
    rerank_score: float


class AskResponse(BaseModel):
    question: str
    answer: str
    sources: list[SourceResponse]


@router.post(
    "/ask",
    response_model=AskResponse
)
def ask(request: AskRequest):

    question = request.question.strip()
    conversation_id = request.conversation_id

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    try:
        result = ask_question(question)

        return result

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Unable to process question: {str(exc)}"
        )