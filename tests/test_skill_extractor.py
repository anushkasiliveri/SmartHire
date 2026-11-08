
import unittest

from src.feature_extraction.skill_extractor import extract_skills


class TestSkillExtractor(unittest.TestCase):

    def test_basic_skill_extraction(self):
        text = "I know Python, SQL and Machine Learning."

        result = extract_skills(text)

        self.assertIn("python", result)
        self.assertIn("sql", result)
        self.assertIn("machine learning", result)

    def test_case_insensitivity(self):
        text = "PYTHON and DATA ANALYSIS"

        result = extract_skills(text)

        self.assertIn("python", result)
        self.assertIn("data analysis", result)

    def test_no_skills_found(self):
        text = "I enjoy reading books and travelling."

        result = extract_skills(text)

        self.assertEqual(result, [])

    def test_special_character_skills(self):
        text = "I have knowledge of C++ and C#."

        result = extract_skills(text)

        self.assertIn("c++", result)
        self.assertIn("c#", result)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_skills(123)


if __name__ == "__main__":
    unittest.main()
