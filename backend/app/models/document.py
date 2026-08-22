from sqlalchemy import Column, Integer, String, Text
from pgvector.sqlalchemy import Vector

from app.database import Base


class DocumentChunk(Base):

    __tablename__ = "document_chunks"

    id = Column(Integer, primary_key=True)

    document_name = Column(
        String,
        nullable=False
    )

    page_number = Column(Integer)

    chunk_index = Column(Integer)

    content = Column(
        Text,
        nullable=False
    )

    embedding = Column(
        Vector(384)
    )