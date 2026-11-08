
from sklearn.feature_extraction.text import TfidfVectorizer


def create_tfidf_features(resume_texts, job_descriptions):
    """
    Convert resume and job description text into numerical TF-IDF features.
    """

    if len(resume_texts) != len(job_descriptions):
        raise ValueError(
            "Resume texts and job descriptions must have equal lengths."
        )

    if not resume_texts:
        raise ValueError("Input text cannot be empty.")

    # Combine resume and job description text
    combined_text = [
        resume + " " + job
        for resume, job in zip(resume_texts, job_descriptions)
    ]

    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=5000
    )

    # Convert text into numerical features
    features = vectorizer.fit_transform(combined_text)

    return features, vectorizer
