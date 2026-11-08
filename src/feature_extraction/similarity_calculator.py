
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(resume_features, job_features):
    """
    Calculate similarity between resume and job description features.
    """

    if resume_features.shape[1] != job_features.shape[1]:
        raise ValueError(
            "Resume and job features must have the same number of columns."
        )

    similarity = cosine_similarity(
        resume_features,
        job_features
    )

    return similarity[0][0] * 100
