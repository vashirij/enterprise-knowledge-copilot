from app.generation.rag_service import ask_question


question = (
    "What is the employee dental insurance deductible?"
)

result = ask_question(question)

print("\nQUESTION")
print(result["question"])

print("\nANSWER")
print(result["answer"])

print("\nSOURCES")

for source in result["sources"]:
    print(
        f"- Document: {source['document']}, "
        f"Page: {source['page']}, "
        f"Chunk: {source['chunk_index']}, "
        f"Rerank Score: {source['rerank_score']:.4f}"
    )