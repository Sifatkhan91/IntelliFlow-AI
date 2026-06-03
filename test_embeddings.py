from app.rag.loaders.router import load_document
from app.rag.chunking import chunk_text
from app.rag.embeddings import create_embeddings
from app.rag.vectorstore import store_embeddings

# Load document
text = load_document("data/sample.pdf")

# Create chunks
chunks = chunk_text(text)

# Create embeddings
embeddings = create_embeddings(chunks)

# Store in vector DB
store_embeddings(chunks, embeddings)

print(f"Stored {len(chunks)} chunks successfully!")