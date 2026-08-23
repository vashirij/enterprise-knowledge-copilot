from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.ingestion.pipeline import ingest_pdf


router = APIRouter(
    prefix="/api/v1/documents",
    tags=["documents"]
)


UPLOAD_DIR = Path("../data/raw")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    original_name = file.filename or "document.pdf"

    safe_name = Path(original_name).name

    unique_name = f"{uuid4().hex}_{safe_name}"

    file_path = UPLOAD_DIR / unique_name

    try:
        contents = await file.read()

        with open(file_path, "wb") as output:
            output.write(contents)

        ingestion_result = ingest_pdf(
            str(file_path)
        )

        return {
            "document": safe_name,
            "stored_as": unique_name,
            "status": "ingested",
            "ingestion": ingestion_result
        }

    except Exception as exc:

        if file_path.exists():
            file_path.unlink()

        raise HTTPException(
            status_code=500,
            detail=f"Document ingestion failed: {str(exc)}"
        )

    finally:
        await file.close()