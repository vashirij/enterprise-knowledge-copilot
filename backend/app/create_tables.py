from app.database import engine, Base
from app.models.document import DocumentChunk

Base.metadata.create_all(bind=engine)

print("Tables created successfully")