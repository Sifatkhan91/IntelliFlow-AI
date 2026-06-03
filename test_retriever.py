from app.rag.retriever import retrieve_relevant_chunks

query = "What is the timing of physics paper?"

results = retrieve_relevant_chunks(query)

print("\nRETRIEVED CHUNKS:\n")

for i, chunk in enumerate(results, start=1):

    print(f"\n--- Result {i} ---\n")

    print(chunk)