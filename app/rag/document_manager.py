from app.rag.vectorstore import collection


def get_all_documents():

    results = collection.get(
        include=["metadatas"]
    )

    documents = set()

    for metadata in results["metadatas"]:

        documents.add(
            metadata["source"]
        )

    return sorted(
        list(documents)
    )
from app.rag.vectorstore import collection


def delete_document(filename):

    results = collection.get(
        where={
            "source": filename
        }
    )

    ids = results["ids"]

    if ids:

        collection.delete(
            ids=ids
        )

        return True

    return False


def get_document_count():

    results = collection.get()

    return len(
        results["ids"]
    )