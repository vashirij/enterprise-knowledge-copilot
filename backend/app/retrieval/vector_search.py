from app.database import SessionLocal
from app.models.document import DocumentChunk
from app.services.embedding_service import embedding_service


def search_documents(
    query: str,
    limit: int = 5,
    min_similarity: float = 0.35
):
    query_embedding = embedding_service.embed_text(query)

    db = SessionLocal()

    try:
        distance = DocumentChunk.embedding.cosine_distance(
            query_embedding
        )

        results = (
            db.query(
                DocumentChunk,
                distance.label("distance")
            )
            .order_by(distance)
            .limit(limit * 2)
            .all()
        )

        filtered_results = []

        for chunk, distance_value in results:

            similarity = 1 - distance_value

            if similarity >= min_similarity:
                filtered_results.append(
                    (chunk, similarity)
                )

            if len(filtered_results) >= limit:
                break

        return filtered_results

    finally:
        db.close()