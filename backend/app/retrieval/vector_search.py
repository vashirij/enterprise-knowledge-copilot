from app.database import SessionLocal
from app.models.document import DocumentChunk
from app.services.embedding_service import embedding_service


def search_documents(
    query: str,
    limit: int = 10
):
    query_embedding = embedding_service.embed_text(query)

    db = SessionLocal()

    try:
        results = (
            db.query(DocumentChunk)
            .order_by(
                DocumentChunk.embedding.cosine_distance(
                    query_embedding
                )
            )
            .limit(limit)
            .all()
        )

        return results

    finally:
        db.close()