from sentence_transformers import SentenceTransformer

# Load embedding model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def create_embeddings(chunks):

    embeddings = embedding_model.encode(chunks)

    return embeddings