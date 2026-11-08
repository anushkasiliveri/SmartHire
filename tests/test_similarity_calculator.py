
import unittest
import numpy as np

from src.feature_extraction.similarity_calculator import (
    calculate_similarity
)


class TestSimilarityCalculator(unittest.TestCase):

    def test_identical_features(self):

        resume_features = np.array([[1, 0, 1]])
        job_features = np.array([[1, 0, 1]])

        result = calculate_similarity(
            resume_features,
            job_features
        )

        self.assertAlmostEqual(result, 100.0)

    def test_different_features(self):

        resume_features = np.array([[1, 0]])
        job_features = np.array([[0, 1]])

        result = calculate_similarity(
            resume_features,
            job_features
        )

        self.assertAlmostEqual(result, 0.0)

    def test_partial_similarity(self):

        resume_features = np.array([[1, 1]])
        job_features = np.array([[1, 0]])

        result = calculate_similarity(
            resume_features,
            job_features
        )

        self.assertGreater(result, 0)
        self.assertLess(result, 100)

    def test_different_feature_dimensions(self):

        resume_features = np.array([[1, 0, 1]])
        job_features = np.array([[1, 0]])

        with self.assertRaises(ValueError):
            calculate_similarity(
                resume_features,
                job_features
            )


if __name__ == "__main__":
    unittest.main()
