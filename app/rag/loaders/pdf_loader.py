from pypdf import PdfReader


def load_pdf(file_path):

    text = ""

    reader = PdfReader(file_path)

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    return text