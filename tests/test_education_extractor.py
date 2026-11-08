
import unittest

from src.feature_extraction.education_extractor import extract_education


class TestEducationExtractor(unittest.TestCase):

    def test_btech_extraction(self):
        text = "I am pursuing B.Tech in Computer Science."

        result = extract_education(text)

        self.assertIn("b.tech", result)

    def test_mba_extraction(self):
        text = "I completed MBA."

        result = extract_education(text)

        self.assertIn("mba", result)

    def test_multiple_qualifications(self):
        text = "B.Tech graduate with an MBA qualification."

        result = extract_education(text)

        self.assertIn("b.tech", result)
        self.assertIn("mba", result)

    def test_no_education_found(self):
        text = "I know Python, Java and SQL."

        result = extract_education(text)

        self.assertEqual(result, [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_education(123)


if __name__ == "__main__":
    unittest.main()
