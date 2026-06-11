from app.rag.vectorstore import collection
from app.memory.memory_manager import load_memory


def get_dashboard_data():

    try:

        data = collection.get()

        documents = list(
            set(
                [
                    item["source"]
                    for item in data["metadatas"]
                ]
            )
        )

        chunks = len(
            data["documents"]
        )

        words = sum(
            len(doc.split())
            for doc in data["documents"]
        )

        memory = load_memory()

        conversations = len(
            memory
        )

        return {
            "documents": len(documents),
            "chunks": chunks,
            "words": words,
            "conversations": conversations
        }

    except Exception:

        return {
            "documents": 0,
            "chunks": 0,
            "words": 0,
            "conversations": 0
        }