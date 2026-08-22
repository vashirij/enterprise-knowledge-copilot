from app.retrieval.vector_search import search_documents
from app.retrieval.reranker import reranker
from app.generation.llm_service import llm_service
from app.generation.prompt_builder import build_rag_prompt


def ask_question(
    question: str,
    candidate_limit: int = 10,
    top_k: int = 3
):

    # 1. Retrieve candidate passages
    candidates = search_documents(
        question,
        limit=candidate_limit
    )

    # 2. Rerank passages
    ranked = reranker.rerank(
        question,
        candidates,
        top_k=top_k
    )

    # 3. Construct grounded RAG prompt
    prompt = build_rag_prompt(
        question,
        ranked
    )

    # 4. Send prompt to local LLM
    answer = llm_service.generate(prompt)

    # 5. Return source metadata
    sources = []

    for chunk, score in ranked:
        sources.append(
            {
                "document": chunk.document_name,
                "page": chunk.page_number,
                "chunk_index": chunk.chunk_index,
                "rerank_score": float(score)
            }
        )

    return {
        "question": question,
        "answer": answer,
        "sources": sources
    }