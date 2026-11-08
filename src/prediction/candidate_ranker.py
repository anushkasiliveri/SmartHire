
def rank_candidates(candidate_results):
    """
    Rank candidates based on their resume similarity scores.
    """

    if not isinstance(candidate_results, list):
        raise TypeError("Candidate results must be a list.")

    for candidate in candidate_results:
        if "similarity_score" not in candidate:
            raise ValueError(
                "Each candidate must have a similarity_score."
            )

        score = candidate["similarity_score"]

        if not isinstance(score, (int, float)):
            raise TypeError(
                "Similarity score must be a number."
            )

    # Sort candidates from highest score to lowest score
    ranked_candidates = sorted(
        candidate_results,
        key=lambda candidate: candidate["similarity_score"],
        reverse=True
    )

    # Assign ranking positions
    for position, candidate in enumerate(
        ranked_candidates, start=1
    ):
        candidate["rank"] = position

    return ranked_candidates
