
import unittest

from src.prediction.resume_matcher import match_resume_to_job


class TestResumeMatcher(unittest.TestCase):

    def test_resume_matching(self):

        resume = """
        Python developer with SQL and Machine Learning skills.
        I have 2 years of experience.
        B.Tech graduate.
        """

        job = """
        Looking for a Python developer with SQL and Machine Learning.
        """

        result = match_resume_to_job(resume, job)

        self.assertGreaterEqual(
            result["similarity_score"], 0
        )

        self.assertIn("python", result["matched_skills"])
        self.assertIn("sql", result["matched_skills"])

    def test_missing_skills(self):

        resume = "Python developer with SQL knowledge."

        job = "Python, SQL and Java developer required."

        result = match_resume_to_job(resume, job)

        self.assertIn("java", result["missing_skills"])

    def test_experience_extraction(self):

        resume = "I have 3 years of experience in Python."

        job = "Python developer required."

        result = match_resume_to_job(resume, job)

        self.assertIn(
            {"value": 3.0, "unit": "years"},
            result["experience"]
        )

    def test_education_extraction(self):

        resume = "I completed B.Tech in Computer Science."

        job = "Python developer required."

        result = match_resume_to_job(resume, job)

        self.assertIn("b.tech", result["education"])

    def test_empty_resume(self):

        with self.assertRaises(ValueError):
            match_resume_to_job(
                "",
                "Python developer required."
            )

    def test_invalid_input(self):

        with self.assertRaises(TypeError):
            match_resume_to_job(
                123,
                "Python developer required."
            )


if __name__ == "__main__":
    unittest.main()
