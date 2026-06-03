import chromadb

# Persistent database storage
client = chromadb.PersistentClient(
    path="chroma_db"
)

# Get or create collection
collection = client.get_or_create_collection(
    name="documents"
)


def store_embeddings(chunks, embeddings):

    for i, (chunk, embedding) in enumerate(
        zip(chunks, embeddings)
    ):

        collection.add(
            documents=[chunk],
            embeddings=[embedding.tolist()],
            ids=[str(i)]
        )

    print("Embeddings stored successfully!")