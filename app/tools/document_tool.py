from app.rag.vectorstore import collection


def list_documents():

    try:

        data = collection.get()

        docs = sorted(
            list(
                set(
                    [
                        item["source"]
                        for item in data["metadatas"]
                    ]
                )
            )
        )

        if not docs:

            return "No documents loaded."

        response = "Loaded Documents:\n\n"

        for i, doc in enumerate(
            docs,
            start=1
        ):

            response += (
                f"{i}. {doc}\n"
            )

        return response

    except Exception as e:

        return str(e)