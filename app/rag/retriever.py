from app.rag.vectorstore import collection
from app.rag.embeddings import embedding_model


def retrieve_relevant_chunks(query, top_k=3):

    # Convert query to embedding
    query_embedding = embedding_model.encode(query)

    # Search vector DB
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )

    return results["documents"][0]