from app.rag.vectorstore import collection


def document_statistics():

    try:

        data = collection.get()

        docs = list(
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

        characters = sum(
            len(doc)
            for doc in data["documents"]
        )

        return f"""
📊 Document Statistics

Documents Loaded: {len(docs)}

Chunks Stored: {chunks}

Total Words: {words}

Total Characters: {characters}
"""

    except Exception as e:

        return f"Error: {str(e)}"