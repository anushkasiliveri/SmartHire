
import re


def clean_resume_text(text):
    """
    Clean extracted resume text for further processing.
    """

    if not isinstance(text, str):
        raise TypeError("Resume text must be a string.")

    # Convert text to lowercase
    text = text.lower()

    # Remove email addresses
    text = re.sub(
        r'\b[\w.+-]+@[\w.-]+\.[a-z]{2,}\b',
        ' ',
        text
    )

    # Remove URLs
    text = re.sub(
        r'https?://\S+|www\.\S+',
        ' ',
        text
    )

    # Remove phone numbers
    text = re.sub(
        r'\+?\d[\d\s().-]{7,}\d',
        ' ',
        text
    )

    # Keep letters, numbers and common technical symbols
    text = re.sub(
        r'[^a-z0-9+#.]',
        ' ',
        text
    )

    # Remove extra spaces and newlines
    text = re.sub(r'\s+', ' ', text)

    return text.strip()
