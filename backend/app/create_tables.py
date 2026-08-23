from app.database import Base, engine

from app.models.document import DocumentChunk
from app.models.conversation import (
    Conversation,
    Message,
)


Base.metadata.create_all(bind=engine)

print("Tables created successfully")