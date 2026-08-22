def build_rag_prompt(question: str, ranked_chunks) -> str:

    context_parts = []

    for chunk, score in ranked_chunks:
        context_parts.append(
            f"""
[{chunk.document_name}, page {chunk.page_number}]

{chunk.content}
"""
        )

    context = "\n".join(context_parts)

    prompt = f"""
SYSTEM:

You are an enterprise knowledge assistant.

Answer questions using ONLY the provided company context.

If the answer is not supported by the provided context, say exactly:

"I do not have sufficient information in the available company documents."

RULES:

1. Do not invent company policies.
2. Do not use outside knowledge.
3. Answer the question briefly and professionally.
4. Only cite sources that support the answer.
5. After the answer, provide the source on a new line.
6. Use exactly this citation format:

Source: <document name>, page <page number>


CONTEXT:

{context}


QUESTION:

{question}


ANSWER:
"""

    return prompt