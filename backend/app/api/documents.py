from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, File, HTTPException, UploadFile
from pydantic import BaseModel
from sqlalchemy import func

from app.database import SessionLocal
from app.ingestion.pipeline import ingest_pdf
from app.models.document import DocumentChunk


router = APIRouter(
    prefix="/api/v1/documents",
    tags=["documents"],
)


# Resolve project root:
# enterprise-knowledge-copilot/
PROJECT_ROOT = Path(__file__).resolve().parents[3]

# Uploaded PDFs:
# enterprise-knowledge-copilot/data/raw/
UPLOAD_DIR = PROJECT_ROOT / "data" / "raw"
UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


ALLOWED_CONTENT_TYPES = {
    "application/pdf",
}


class DocumentResponse(BaseModel):
    id: int
    document_name: str
    pages: int
    chunks: int


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):
    """
    Upload and ingest a PDF into the knowledge base.

    Pipeline:
    PDF upload
        -> save file
        -> parse PDF
        -> semantic chunking
        -> embeddings
        -> pgvector storage
    """

    # Validate MIME type
    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported.",
        )

    # Prevent directory traversal
    original_name = (
        file.filename
        or "document.pdf"
    )

    safe_name = Path(
        original_name
    ).name

    # Validate extension
    if Path(safe_name).suffix.lower() != ".pdf":
        raise HTTPException(
            status_code=400,
            detail="Uploaded file must have a .pdf extension.",
        )

    # Generate unique storage name
    unique_name = (
        f"{uuid4().hex}_{safe_name}"
    )

    file_path = (
        UPLOAD_DIR
        / unique_name
    )

    try:
        contents = await file.read()

        if not contents:
            raise HTTPException(
                status_code=400,
                detail="Uploaded PDF is empty.",
            )

        # Store locally
        file_path.write_bytes(
            contents
        )

        # Run ingestion
        ingestion_result = ingest_pdf(
            str(file_path)
        )

        return {
            "document": safe_name,
            "stored_as": unique_name,
            "status": "ingested",
            "ingestion": ingestion_result,
        }

    except HTTPException:

        if file_path.exists():
            file_path.unlink()

        raise

    except Exception as exc:

        if file_path.exists():
            file_path.unlink()

        raise HTTPException(
            status_code=500,
            detail=(
                "Document ingestion failed: "
                f"{str(exc)}"
            ),
        ) from exc

    finally:
        await file.close()


@router.get(
    "",
    response_model=list[DocumentResponse],
)
def list_documents():
    """
    Return all documents currently represented
    in document_chunks.

    Since we currently do not have a separate
    documents table, the first chunk ID is used
    as the temporary document ID.
    """

    db = SessionLocal()

    try:
        documents = (
            db.query(
                func.min(
                    DocumentChunk.id
                ).label("id"),

                DocumentChunk.document_name,

                func.max(
                    DocumentChunk.page_number
                ).label("pages"),

                func.count(
                    DocumentChunk.id
                ).label("chunks"),
            )
            .group_by(
                DocumentChunk.document_name
            )
            .order_by(
                DocumentChunk.document_name
            )
            .all()
        )

        return [
            {
                "id": document.id,
                "document_name":
                    document.document_name,
                "pages":
                    document.pages or 0,
                "chunks":
                    document.chunks,
            }
            for document in documents
        ]

    finally:
        db.close()


@router.delete(
    "/{document_id}"
)
def delete_document(
    document_id: int
):
    """
    Delete all chunks belonging to a document.

    document_id currently refers to the ID
    of one of that document's chunks.
    """

    db = SessionLocal()

    try:
        chunk = (
            db.query(
                DocumentChunk
            )
            .filter(
                DocumentChunk.id
                == document_id
            )
            .first()
        )

        if not chunk:
            raise HTTPException(
                status_code=404,
                detail="Document not found.",
            )

        document_name = (
            chunk.document_name
        )

        deleted_count = (
            db.query(
                DocumentChunk
            )
            .filter(
                DocumentChunk.document_name
                == document_name
            )
            .delete(
                synchronize_session=False
            )
        )

        db.commit()

        return {
            "document":
                document_name,
            "status":
                "deleted",
            "chunks_deleted":
                deleted_count,
        }

    except HTTPException:
        db.rollback()
        raise

    except Exception as exc:
        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=(
                "Unable to delete document: "
                f"{str(exc)}"
            ),
        ) from exc

    finally:
        db.close()