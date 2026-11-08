
import re


def extract_experience(text):
    """
    Extract work experience from resume text.
    """

    if not isinstance(text, str):
        raise TypeError("Input text must be a string.")

    text = text.lower()

    experience = []

    # Find experience expressed in years
    year_pattern = r'(\d+(?:\.\d+)?)\s*\+?\s*(?:years?|yrs?)'

    years = re.findall(year_pattern, text)

    for year in years:
        experience.append({
            "value": float(year),
            "unit": "years"
        })

    # Find experience expressed in months
    month_pattern = r'(\d+)\s*\+?\s*(?:months?|mos?)'

    months = re.findall(month_pattern, text)

    for month in months:
        experience.append({
            "value": float(month),
            "unit": "months"
        })

    return experience
