from app.retrieval.vector_search import search_documents


query = "How much vacation can employees carry over?"

results = search_documents(query)

for chunk, similarity in results:
    print(
        f"Similarity: {similarity:.2f}, "
        f"Document: {chunk.document_name}, "
        f"Page: {chunk.page_number}, "
        f"Chunk Index: {chunk.chunk_index}, "
        f"Content: {chunk.content}"
    )
