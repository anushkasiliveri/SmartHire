
import unittest

from src.feature_extraction.experience_extractor import extract_experience


class TestExperienceExtractor(unittest.TestCase):

    def test_year_experience(self):
        text = "I have 3 years of experience in Python."

        result = extract_experience(text)

        self.assertIn(
            {"value": 3.0, "unit": "years"},
            result
        )

    def test_month_experience(self):
        text = "I have 6 months of internship experience."

        result = extract_experience(text)

        self.assertIn(
            {"value": 6.0, "unit": "months"},
            result
        )

    def test_multiple_experiences(self):
        text = "3 years of experience and 6 months of internship."

        result = extract_experience(text)

        self.assertEqual(len(result), 2)

    def test_no_experience(self):
        text = "I know Python and SQL."

        result = extract_experience(text)

        self.assertEqual(result, [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_experience(123)


if __name__ == "__main__":
    unittest.main()
