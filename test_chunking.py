from app.rag.loaders.router import load_document
from app.rag.chunking import chunk_text

# Load document
text = load_document("data/sample.pdf")

# Create chunks
chunks = chunk_text(text)

# Print results
print(f"Total chunks: {len(chunks)}")

print("\nFIRST CHUNK:\n")
print(chunks[0])