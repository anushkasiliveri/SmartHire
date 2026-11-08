
import re


# List of technical skills to identify
SKILL_LIST = [
    "python",
    "java",
    "c++",
    "c#",
    "javascript",
    "html",
    "css",
    "sql",
    "mysql",
    "mongodb",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data analysis",
    "data science",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "opencv",
    "flask",
    "django",
    "streamlit",
    "git",
    "github",
    "power bi",
    "tableau",
    "excel",
    "aws",
    "azure",
    "communication",
]


def extract_skills(text):
    """
    Identify skills present in resume text.
    """

    if not isinstance(text, str):
        raise TypeError("Input text must be a string.")

    text = text.lower()

    detected_skills = []

    for skill in SKILL_LIST:

        pattern = r'(?<!\w)' + re.escape(skill) + r'(?!\w)'

        if re.search(pattern, text):
            detected_skills.append(skill)

    return detected_skills
