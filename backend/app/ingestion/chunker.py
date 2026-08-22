import re
import numpy as np

from app.services.embedding_service import embedding_service


def split_into_sentences(text: str):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    return [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )


def semantic_chunk_text(
    text: str,
    similarity_threshold: float = 0.55,
    max_sentences: int = 6
):
    sentences = split_into_sentences(text)

    if not sentences:
        return []

    embeddings = [
        embedding_service.embed_text(sentence)
        for sentence in sentences
    ]

    chunks = []

    current_chunk = [sentences[0]]

    for i in range(1, len(sentences)):

        previous_embedding = embeddings[i - 1]
        current_embedding = embeddings[i]

        similarity = cosine_similarity(
            previous_embedding,
            current_embedding
        )

        if (
            similarity >= similarity_threshold
            and len(current_chunk) < max_sentences
        ):
            current_chunk.append(sentences[i])

        else:
            chunks.append(
                " ".join(current_chunk)
            )

            current_chunk = [sentences[i]]

    if current_chunk:
        chunks.append(
            " ".join(current_chunk)
        )

    return chunks