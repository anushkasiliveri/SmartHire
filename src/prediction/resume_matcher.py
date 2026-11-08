
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.data_processing.text_cleaner import clean_resume_text
from src.feature_extraction.skill_extractor import extract_skills
from src.feature_extraction.experience_extractor import extract_experience
from src.feature_extraction.education_extractor import extract_education


def match_resume_to_job(resume_text, job_description):
    """
    Compare a resume with a job description and return matching details.
    """

    if not isinstance(resume_text, str):
        raise TypeError("Resume text must be a string.")

    if not isinstance(job_description, str):
        raise TypeError("Job description must be a string.")

    # Clean resume and job description
    clean_resume = clean_resume_text(resume_text)
    clean_job = clean_resume_text(job_description)

    if not clean_resume or not clean_job:
        raise ValueError(
            "Resume and job description cannot be empty."
        )

    # Convert both documents into TF-IDF features
    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=5000
    )

    features = vectorizer.fit_transform(
        [clean_resume, clean_job]
    )

    # Calculate cosine similarity
    similarity = cosine_similarity(
        features[0:1],
        features[1:2]
    )[0][0]

    similarity_score = round(similarity * 100, 2)

    # Extract skills
    resume_skills = extract_skills(resume_text)
    required_skills = extract_skills(job_description)

    # Find matching and missing skills
    matched_skills = [
        skill for skill in required_skills
        if skill in resume_skills
    ]

    missing_skills = [
        skill for skill in required_skills
        if skill not in resume_skills
    ]

    # Extract experience and education
    experience = extract_experience(resume_text)
    education = extract_education(resume_text)

    return {
        "similarity_score": similarity_score,
        "resume_skills": resume_skills,
        "required_skills": required_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "experience": experience,
        "education": education
    }
