
import re


EDUCATION_LIST = [
    "b.tech",
    "btech",
    "b.e.",
    "be",
    "m.tech",
    "mtech",
    "m.e.",
    "me",
    "b.sc",
    "bsc",
    "m.sc",
    "msc",
    "bca",
    "mca",
    "mba",
    "ph.d",
    "phd",
    "diploma",
]


def extract_education(text):
    """
    Identify educational qualifications in resume text.
    """

    if not isinstance(text, str):
        raise TypeError("Input text must be a string.")

    text = text.lower()

    detected_education = []

    for qualification in EDUCATION_LIST:

        pattern = r'(?<!\w)' + re.escape(qualification) + r'(?!\w)'

        if re.search(pattern, text):
            detected_education.append(qualification)

    return detected_education
