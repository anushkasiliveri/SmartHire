
import unittest

from src.feature_extraction.text_vectorizer import create_tfidf_features


class TestTextVectorizer(unittest.TestCase):

    def test_feature_creation(self):

        resumes = [
            "Python developer with SQL knowledge",
            "Java developer with database knowledge"
        ]

        jobs = [
            "Python and SQL developer required",
            "Java and database developer required"
        ]

        features, vectorizer = create_tfidf_features(
            resumes, jobs
        )

        self.assertEqual(features.shape[0], 2)
        self.assertGreater(features.shape[1], 0)

    def test_equal_input_lengths(self):

        resumes = ["Python developer"]
        jobs = ["Python required", "SQL required"]

        with self.assertRaises(ValueError):
            create_tfidf_features(resumes, jobs)

    def test_empty_input(self):

        with self.assertRaises(ValueError):
            create_tfidf_features([], [])

    def test_vectorizer_creation(self):

        resumes = ["Python developer"]
        jobs = ["Python required"]

        features, vectorizer = create_tfidf_features(
            resumes, jobs
        )

        self.assertIsNotNone(vectorizer)
        self.assertEqual(features.shape[0], 1)


if __name__ == "__main__":
    unittest.main()
