from app.services.ingestion import load_file, chunk_documents
from pathlib import Path
docs = load_file(Path(r"data\sample_data\company_hr_handbook.md"))
chunked_docs = chunk_documents(docs)
print(chunked_docs)