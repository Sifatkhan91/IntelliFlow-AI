from pathlib import Path

from app.rag.loaders.router import load_document
from app.rag.chunking import chunk_text
from app.rag.embeddings import create_embeddings
from app.rag.vectorstore import store_embeddings


def ingest_document(file_path):

    filename = Path(file_path).name

    print("\n" + "=" * 60)
    print(f"Ingesting: {filename}")
    print("=" * 60)

    text = load_document(file_path)

    if not text or len(text.strip()) < 20:

        raise ValueError(
            f"No readable text found in "
            f"'{filename}'."
        )

    print(
        f"Text length: {len(text)}"
    )

    chunks = chunk_text(text)

    print(
        f"Chunks created: {len(chunks)}"
    )

    if len(chunks) == 0:

        raise ValueError(
            f"No chunks created from "
            f"'{filename}'."
        )

    embeddings = create_embeddings(
        chunks
    )

    print(
        f"Embeddings created: "
        f"{len(embeddings)}"
    )

    store_embeddings(
        chunks,
        embeddings,
        filename
    )

    print(
        f"Document stored: {filename}"
    )

    return len(chunks)