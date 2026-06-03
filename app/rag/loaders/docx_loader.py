from docx import Document


def load_docx(file_path):

    doc = Document(file_path)

    text = "\n".join(
        [paragraph.text for paragraph in doc.paragraphs]
    )

    return text