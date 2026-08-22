from app.retrieval.vector_search import search_documents
from app.retrieval.reranker import reranker


query = (
    "What is the maximum number of hours a student employee "
    "can work while classes are in session?"
)

candidates = search_documents(
    query,
    limit=10
)

ranked = reranker.rerank(
    query,
    candidates,
    top_k=3
)


print(f"\nQuery: {query}")

for rank, (chunk, score) in enumerate(ranked, start=1):

    print("\n----------------")
    print(f"Rank: {rank}")
    print(f"Rerank Score: {float(score):.4f}")
    print(f"Document: {chunk.document_name}")
    print(f"Page: {chunk.page_number}")
    print(f"Chunk Index: {chunk.chunk_index}")
    print(f"Content:\n{chunk.content}")