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

If the answer is not supported by the provided context,
say:

"I do not have sufficient information in the available company documents."

Do not invent company policies.

Do not use outside knowledge.

Provide the source document and page number.

Keep the answer concise and professional.


CONTEXT:

{context}


QUESTION:

{question}


ANSWER:
"""

    return prompt