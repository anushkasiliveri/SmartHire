
from pypdf import PdfReader


def extract_resume_text(uploaded_file):
    """
    Extract readable text from PDF or TXT resumes.
    """

    file_name = uploaded_file.name.lower()

    # Extract text from PDF files
    if file_name.endswith(".pdf"):

        pdf_reader = PdfReader(uploaded_file)

        extracted_text = ""

        for page in pdf_reader.pages:
            page_text = page.extract_text()

            if page_text:
                extracted_text += page_text + "\n"

    # Extract text from TXT files
    elif file_name.endswith(".txt"):

        extracted_text = uploaded_file.getvalue().decode(
            "utf-8", errors="ignore"
        )

    else:
        raise ValueError("Only PDF and TXT files are supported.")

    # Check whether text was extracted
    extracted_text = extracted_text.strip()

    if not extracted_text:
        raise ValueError(
            "No readable text found in the resume."
        )

    return extracted_text
