from app.rag.vectorstore import collection
from app.rag.embeddings import embedding_model


def retrieve_relevant_chunks(
    query,
    active_document=None,
    top_k=10
):

    query_embedding = (
        embedding_model.encode(query)
    )

    if active_document:

        results = collection.query(
            query_embeddings=[
                query_embedding.tolist()
            ],
            n_results=top_k,
            where={
                "source": active_document
            }
        )

    else:

        results = collection.query(
            query_embeddings=[
                query_embedding.tolist()
            ],
            n_results=top_k
        )

    documents = results["documents"][0]

    metadata = results["metadatas"][0]

    sources = list(
        {
            item["source"]
            for item in metadata
        }
    )

    return {
    "documents": documents,
    "metadata": metadata,
    "sources": sources
}