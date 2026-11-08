
import unittest

from src.prediction.candidate_ranker import rank_candidates


class TestCandidateRanker(unittest.TestCase):

    def test_candidate_ranking(self):

        candidates = [
            {"name": "Rahul", "similarity_score": 85},
            {"name": "Priya", "similarity_score": 92},
            {"name": "Arjun", "similarity_score": 67}
        ]

        result = rank_candidates(candidates)

        self.assertEqual(result[0]["name"], "Priya")
        self.assertEqual(result[1]["name"], "Rahul")
        self.assertEqual(result[2]["name"], "Arjun")

    def test_rank_assignment(self):

        candidates = [
            {"name": "Rahul", "similarity_score": 85},
            {"name": "Priya", "similarity_score": 92}
        ]

        result = rank_candidates(candidates)

        self.assertEqual(result[0]["rank"], 1)
        self.assertEqual(result[1]["rank"], 2)

    def test_empty_candidate_list(self):

        result = rank_candidates([])

        self.assertEqual(result, [])

    def test_missing_similarity_score(self):

        candidates = [
            {"name": "Rahul"}
        ]

        with self.assertRaises(ValueError):
            rank_candidates(candidates)

    def test_invalid_input(self):

        with self.assertRaises(TypeError):
            rank_candidates("invalid")

    def test_invalid_score(self):

        candidates = [
            {"name": "Rahul", "similarity_score": "high"}
        ]

        with self.assertRaises(TypeError):
            rank_candidates(candidates)


if __name__ == "__main__":
    unittest.main()
