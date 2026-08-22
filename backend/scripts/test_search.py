from app.retrieval.vector_search import search_documents


query = "How much vacation can employees carry over?"

results = search_documents(query)


for result in results:

    print("\n----------------")

    print(
        f"Source: {result.document_name}"
    )

    print(
        f"Page: {result.page_number}"
    )

    print(result.content)