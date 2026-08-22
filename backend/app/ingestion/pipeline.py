from pathlib import Path

from app.database import SessionLocal
from app.models.document import DocumentChunk
from app.ingestion.pdf_parser import parse_pdf
from app.ingestion.chunker import chunk_text
from app.services.embedding_service import embedding_service


def ingest_pdf(file_path: str):

    db = SessionLocal()

    try:

        pages = parse_pdf(file_path)

        document_name = Path(file_path).name

        total_chunks = 0

        for page in pages:

            chunks = chunk_text(
                page["text"]
            )

            for chunk_index, chunk in enumerate(chunks):

                embedding = embedding_service.embed_text(
                    chunk
                )

                record = DocumentChunk(
                    document_name=document_name,
                    page_number=page["page_number"],
                    chunk_index=chunk_index,
                    content=chunk,
                    embedding=embedding
                )

                db.add(record)

                total_chunks += 1

        db.commit()

        print(
            f"Ingested {document_name}: "
            f"{total_chunks} chunks"
        )

    finally:

        db.close()