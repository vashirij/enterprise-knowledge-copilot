from datetime import datetime, timezone

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)

from sqlalchemy.orm import relationship

from app.database import Base


class Conversation(Base):

    __tablename__ = "conversations"

    id = Column(
        Integer,
        primary_key=True
    )

    title = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=lambda:
            datetime.now(timezone.utc)
    )

    updated_at = Column(
        DateTime,
        default=lambda:
            datetime.now(timezone.utc)
    )

    messages = relationship(
        "Message",
        back_populates="conversation",
        cascade="all, delete-orphan"
    )


class Message(Base):

    __tablename__ = "messages"

    id = Column(
        Integer,
        primary_key=True
    )

    conversation_id = Column(
        Integer,
        ForeignKey(
            "conversations.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    role = Column(
        String,
        nullable=False
    )

    content = Column(
        Text,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=lambda:
            datetime.now(timezone.utc)
    )

    conversation = relationship(
        "Conversation",
        back_populates="messages"
    )