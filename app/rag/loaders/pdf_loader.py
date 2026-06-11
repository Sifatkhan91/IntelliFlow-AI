import fitz
import pytesseract

from PIL import Image


# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def load_pdf(file_path):

    doc = fitz.open(file_path)

    full_text = ""

    print("\n===== OCR PDF LOADER =====")

    for page_num in range(len(doc)):

        page = doc.load_page(page_num)

        # Try normal extraction first
        text = page.get_text()

        if text.strip():

            print(
                f"Page {page_num + 1}: "
                f"Normal text extracted"
            )

            full_text += text + "\n"

        else:

            print(
                f"Page {page_num + 1}: "
                f"OCR required"
            )

            pix = page.get_pixmap(
                matrix=fitz.Matrix(2, 2)
            )

            img = Image.frombytes(
                "RGB",
                [pix.width, pix.height],
                pix.samples
            )

            ocr_text = pytesseract.image_to_string(
                img
            )

            full_text += ocr_text + "\n"

    print(
        f"\nTOTAL TEXT LENGTH: "
        f"{len(full_text)}"
    )

    print("==========================\n")

    return full_text