import uuid
import chromadb


client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_or_create_collection(
    name="documents"
)


def store_embeddings(
    chunks,
    embeddings,
    filename
):

    if len(chunks) == 0:
        raise ValueError(
            "Chunks list is empty."
        )

    if len(embeddings) == 0:
        raise ValueError(
            "Embeddings list is empty."
        )

    ids = [
        str(uuid.uuid4())
        for _ in chunks
    ]

    metadatas = [

    {
        "source": filename,
        "chunk_id": i
    }

    for i in range(
        len(chunks)
    )

]

    collection.add(
        documents=chunks,
        embeddings=[
            embedding.tolist()
            for embedding in embeddings
        ],
        metadatas=metadatas,
        ids=ids
    )

    print(
        f"{len(chunks)} chunks stored for {filename}"
    )