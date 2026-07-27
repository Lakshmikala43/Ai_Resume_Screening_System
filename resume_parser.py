import pdfplumber


def extract_text_from_pdf(pdf_path):
    """
    Extract all text from a PDF resume.
    """

    text = ""

    try:

        with pdfplumber.open(pdf_path) as pdf:

            # Loop through every page
            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:

                    text += page_text + "\n"

    except Exception as e:

        print("Error reading PDF:", e)

    return text