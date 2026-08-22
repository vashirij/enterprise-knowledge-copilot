from pypdf import PdfReader


def parse_pdf(file_path: str):

    reader = PdfReader(file_path)

    pages = []

    for page_number, page in enumerate(reader.pages):

        text = page.extract_text()

        if text:

            pages.append(
                {
                    "page_number": page_number + 1,
                    "text": text
                }
            )

    return pages