from app.rag.loaders.router import load_document

file_path = "data/sample.pdf"

text = load_document(file_path)

print(text[:1000])